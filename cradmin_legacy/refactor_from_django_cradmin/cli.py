import difflib
import fnmatch
import os
import re
import sys

import fire

from cradmin_legacy.refactor_from_django_cradmin import colorize


class AbstractReplace(object):
    def replace(self, string):
        raise NotImplementedError()


class StringReplace(AbstractReplace):
    def __init__(self, from_string, to_string):
        self.from_string = from_string
        self.to_string = to_string

    def replace(self, string):
        return string.replace(self.from_string, self.to_string)


class RegexReplace(AbstractReplace):
    def __init__(self, pattern, replacement):
        self.pattern = re.compile(pattern, re.MULTILINE)
        self.replacement = replacement

    def replace(self, string):
        new_string, number_of_replacements = self.pattern.subn(self.replacement, string)
        return new_string


class AbstractRefactorFile(object):
    replacers = []

    def __init__(self, filepath):
        self.filepath = filepath
        self.original_filecontent = open(self.filepath, 'rb').read().decode('utf-8')
        self.new_filecontent = self._refactor_to_string()

    def did_update(self):
        return self.original_filecontent != self.new_filecontent

    def _refactor_to_string(self):
        new_string = self.original_filecontent
        for replacer in self.replacers:
            new_string = replacer.replace(new_string)
        return new_string

    def refactor(self):
        with open(self.filepath, 'wb') as f:
            f.write(self.new_filecontent.encode('utf-8'))

    def iter_difflines(self):
        difflist = list(difflib.Differ().compare(
            self.original_filecontent.splitlines(keepends=True),
            self.new_filecontent.splitlines(keepends=True)))
        for diffline in difflist:
            if diffline.startswith(' '):
                continue
            yield diffline

    def print_diff(self):
        if not self.did_update():
            return
        print(colorize.colored_text('{}:'.format(self.filepath), colorize.COLOR_BLUE, bold=True))
        for diffline in self.iter_difflines():
            if diffline.startswith('+'):
                color = colorize.COLOR_GREEN
            elif diffline.startswith('-'):
                color = colorize.COLOR_RED
            else:
                color = colorize.COLOR_GREY
            sys.stdout.write(colorize.colored_text(diffline, color))


class RefactorPythonFile(AbstractRefactorFile):
    replacers = [
        RegexReplace(r'django_cradmin(\.|\/)', r'cradmin_legacy\1'),
        RegexReplace(r'import\s+django_cradmin', r'import cradmin_legacy'),
    ]


class Cli(object):
    """
    Migrate a codebase using django_cradmin 1x to using cradmin_legacy.
    """
    def _make_exclude_directories(self, extra_exclude_directories):
        exclude_directories = [
            '**/node_modules',
            '.git',
            '**/.git',
        ]
        exclude_directories.extend(exclude_directories)
        return exclude_directories

    def _fnmatch_many(self, path, patterns):
        for pattern in patterns:
            if fnmatch.fnmatch(path, pattern):
                return True
        return False

    def __iter_walk_directory(self, toplevel_directory,
                              filepatterns,
                              include_files=False,
                              include_directories=False,
                              exclude_directories=tuple()):
        exclude_directories = self._make_exclude_directories(exclude_directories)

        for directory, subdirectories, filenames in os.walk(toplevel_directory):
            for subdirectory in subdirectories:
                subdirectorypath = os.path.join(directory, subdirectory)
                if self._fnmatch_many(subdirectorypath, exclude_directories):
                    subdirectories.remove(subdirectory)
                elif include_directories:
                    yield subdirectorypath
            if include_files:
                for filename in filenames:
                    filepath = os.path.join(directory, filename)
                    if os.path.islink(filepath):
                        continue
                    if self._fnmatch_many(filepath, filepatterns):
                        yield filepath

    def _refactor_python_file(self, filepath, verbose=False, pretend=False):
        refactor = RefactorPythonFile(filepath=filepath)
        if verbose:
            refactor.print_diff()

    def refactor_python_code(self, directory, exclude_directories=tuple(), verbose=False, pretend=False):
        """
        Refactor .py files.

        --directory
            The directory to refactory. Typically the root module directory
            for the project that uses django_cradmin 1x.
        --exclude-directories
            Add extra fnmatch/glob exclude patterns for directories.
            The default exclude patterns are ['**/node_modules', '.git', '**/.git'].

            Example: ``--exclude-directories "('libs/*', 'extrastuff/*')"``.

            We do not follow symlinks when refactoring, so you do not
            have to exclude symlinked directories.
        """
        for filepath in self.__iter_walk_directory(
                toplevel_directory=directory,
                filepatterns=['*.py'],
                include_files=True,
                exclude_directories=exclude_directories):
            self._refactor_python_file(filepath=filepath, verbose=verbose)

    def refactor_rst_code(self, directory, exclude_directories=tuple(), verbose=False, pretend=False):
        """
        Refactor .rst files.

        --directory
            The directory to refactory. Typically the root module directory
            for the project that uses django_cradmin 1x.
        --exclude-directories
            Add extra fnmatch/glob exclude patterns for directories.
            The default exclude patterns are ['**/node_modules', '.git', '**/.git'].

            Example: ``--exclude-directories "('libs/*', 'extrastuff/*')"``.

            We do not follow symlinks when refactoring, so you do not
            have to exclude symlinked directories.
        """
        for filepath in self.__iter_walk_directory(
                toplevel_directory=directory,
                filepatterns=['*.rst'],
                include_files=True,
                exclude_directories=exclude_directories):
            self._refactor_python_file(filepath=filepath, verbose=verbose,
                                       pretend=False)

    def refactor_all(self, directory, exclude_directories=tuple(), verbose=False, pretend=False):
        self.refactor_python_code(directory=directory, exclude_directories=exclude_directories,
                                  verbose=verbose, pretend=pretend)
        self.refactor_rst_code(directory=directory, exclude_directories=exclude_directories,
                               verbose=verbose, pretend=pretend)

    # def detect_dangerous_code(self, directory, cradmin_version, exclude_directories=tuple()):
    #     """
    #     Detect dangerous code that requires some special handling.
    #
    #     Prints out warning messages for detected dangerous code.
    #
    #     --directory
    #         The directory to detect code in. Typically the root directory of the repository
    #         of a project using django-cradmin.
    #     --cradmin-version
    #         The version of django-cradmin that the codebase you are checking is using.
    #         Examples:
    #             --cradmin-version "1.2.3"
    #             --cradmin-version "2.3.1"
    #     --exclude-directories
    #         Add extra fnmatch/glob exclude patterns for directories.
    #         The default exclude patterns are ['**/node_modules', '.git', '**/.git'].
    #
    #         Example: ``--exclude-directories "('libs/*', 'extrastuff/*')"``.
    #
    #         We do not follow symlinks when refactoring, so you do not
    #         have to exclude symlinked directories.
    #     """
    #     for filepath in self.__iter_walk_directory(
    #             toplevel_directory=directory,
    #             filepatterns=['*.rst', '*.py'],
    #             include_files=True,
    #             exclude_directories=exclude_directories):
    #         if filepath.endswith('.py'):
    #             detector = detect_dangerous_code.DetectDangerousPythonCode(
    #                 filepath=filepath,
    #                 cradmin_version=cradmin_version
    #             )
    #             detector.print_messages()


def main():
    fire.Fire(Cli)


if __name__ == '__main__':
    main()
