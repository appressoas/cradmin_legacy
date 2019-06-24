##############################################
How to release a new version of cradmin legacy
##############################################

.. note:: This assumes you have permission to release cradmin to pypi.

1. Update ``django_cradmin/version.json``.
2. Commit with ``Release <version>``.
3. Tag the commit with ``<version>``.
4. Push (``git push && git push --tags``).
5. Release to pypi (``python setup.py sdist && twine upload dist/cradmin-legacy<version>.tar.gz``).
