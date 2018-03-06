# import re
# import textwrap
#
# from cradmin_legacy.refactor_from_django_cradmin import colorize
#
#
# class AbstractDetector(object):
#     def __init__(self, message):
#         self.message = message
#
#     def get_detection_method_description(self):
#         raise NotImplementedError()
#
#     def get_message(self):
#         return '{} ({})'.format(self.message, self.get_detection_method_description())
#
#     def detect(self, string):
#         raise NotImplementedError()
#
#
# class RegexDetector(AbstractDetector):
#     def __init__(self, pattern, message):
#         super(RegexDetector, self).__init__(message=message)
#         self.pattern_string = pattern
#         self.pattern = re.compile(pattern, re.MULTILINE)
#
#     def get_detection_method_description(self):
#         return 'matches regex: {!r}'.format(self.pattern_string)
#
#     def detect(self, string):
#         return self.pattern.search(string) is not None
#
#
# class AbstractDetectDangerousCode(object):
#     def __init__(self, filepath, cradmin_version):
#         self.filepath = filepath
#         self.cradmin_version = cradmin_version
#         self.filecontent = open(self.filepath, 'rb').read().decode('utf-8')
#         self.messages = []
#         self._detect()
#
#     def get_detectors(self):
#         raise NotImplementedError()
#
#     def _detect(self):
#         self.messages = []
#         for detector in self.get_detectors():
#             if detector.detect(self.filecontent):
#                 self.messages.append(detector.get_message())
#
#     def print_messages(self):
#         if not self.messages:
#             return
#         print(colorize.colored_text('{}:'.format(self.filepath), colorize.COLOR_GREY, bold=True))
#         textwrapper = textwrap.TextWrapper(initial_indent='  - ', subsequent_indent='    ', width=100)
#         for message in self.messages:
#             formatted_message = textwrapper.fill(message)
#             print(colorize.colored_text(formatted_message, colorize.COLOR_RED))
#
#
# class DetectDangerousPythonCode(AbstractDetectDangerousCode):
#     def get_detectors(self):
#         detectors = [
#             # RegexDetector('cradmin_generic_token_with_metadata',
#             #               'cradmin_generic_token_with_metadata is not available in django_cradmin >= 4.0.0 - '
#             #               'or in cradmin_legacy. It has been moved to '
#             #               'ievv_opensource.ievv_generic_token_with_metadata.\n\n'
#             #               'You will normally not need to datamigrate generic tokens, since they are normally '
#             #               'short lived, but if you need to do that, it is documented in the '
#             #               'documentation for ievv_opensource.ievv_generic_token_with_metadata.\n\n'
#             #               '`cradmin_legacy_refactor_from_django_cradmin refactor-python-code` refactors '
#             #               'cradmin_generic_token_with_metadata automatically to '
#             #               'ievv_opensource.ievv_generic_token_with_metadata, so as long as you update '
#             #               'to ievv-opensource>=5.0.0, and you do not care that you will loose all '
#             #               'GenericTokenWithMetadata objects, you can ignore this warning.'),
#         ]
#         if self.cradmin_version >= '2.0.0':
#             detectors.extend([
#                 # RegexDetector('cradmin_temporaryfileuploadstore',
#                 #               'cradmin_temporaryfileuploadstore is not available in django_cradmin >= 4.0.0'),
#                 # RegexDetector('cradmin_imagearchive',
#                 #               'cradmin_imagearchive is not available in django_cradmin >= 4.0.0'),
#             ])
#         else:
#             detectors.extend([
#             ])
#         return detectors
