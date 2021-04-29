##############################################
How to release a new version of cradmin legacy
##############################################

.. note:: This assumes you have permission to release cradmin to pypi.

1. Update ``django_cradmin/version.json``.
2. Add releasenote to `docs/releasenotes`.
3. Commit with ``Release <version>``.
4. Tag the commit with ``<version>``.
5. Push (``git push && git push --tags``).
6. Release to pypi (``python setup.py sdist && twine upload dist/cradmin-legacy-<version>.tar.gz``).
