##########################
Javascript - develop/build
##########################

First go to the javascript source directory and install the dependencies::

    $ cd cradmin_legacy/static/cradmin_legacy
    $ yarn


Then run grunt to build. During development you can use::

    $ node_modules/.bin/grunt watch


For release, use::

    $ node_modules/.bin/grunt dist
