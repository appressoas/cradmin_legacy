########
Settings
########

.. setting:: CRADMIN_LEGACY_THEME_PATH

CRADMIN_LEGACY_THEME_PATH
=========================
The staticfiles path to the theme CSS. If this is not
set, we use ``cradmin_legacy/dist/css/cradmin_theme_default/theme.css``.


.. setting::  CRADMIN_LEGACY_CSS_ICON_MAP

CRADMIN_LEGACY_CSS_ICON_MAP
===========================
A dictionary mapping generalized icon names to css classes.
It is used by the ``cradmin_icon`` template tag. If you do
not set this, you will get font-awesome icons as defined
in :obj:`.cradmin_legacy.css_icon_map.FONT_AWESOME`.

.. seealso:: :ref:`cradmin_icon_tags` and :issue:`43`.


.. setting::  CRADMIN_LEGACY_CSS_ICON_LIBRARY_PATH

CRADMIN_LEGACY_CSS_ICON_LIBRARY_PATH
====================================
The staticfiles path to the css icon library.
Defaults to ``"cradmin_legacy/dist/vendor/fonts/fontawesome/css/font-awesome.min.css"``.


.. setting:: CRADMIN_LEGACY_HIDE_PAGEHEADER_IN_FORMVIEWS

CRADMIN_LEGACY_HIDE_PAGEHEADER_IN_FORMVIEWS
===========================================
Can be used to hide the page header in form views by default.


.. setting:: CRADMIN_LEGACY_HIDE_PAGEHEADER_IN_LISTINGVIEWS

CRADMIN_LEGACY_HIDE_PAGEHEADER_IN_LISTINGVIEWS
==============================================
Can be used to hide the page header in listing views by default.


.. setting:: CRADMIN_LEGACY_MENU_SCROLL_TOP_FIXED

CRADMIN_LEGACY_MENU_SCROLL_TOP_FIXED
====================================
If this is ``True``, the menu template will add an angularjs directive that
automatically scrolls the menu when the window is scrolled.


.. setting:: CRADMIN_LEGACY_HIDE_PAGE_HEADER

CRADMIN_LEGACY_HIDE_PAGE_HEADER
===============================
If this is ``True``, we do not render the page header. This only affects views
that use templates inheriting from the ``cradmin_legacy/standalone-base.django.html``
template. This means all the views in ``cradmin_legacy.viewhelpers``, but not the login
views, or other standalone (non-crapp.App views).


**********
imageutils
**********

.. setting:: CRADMIN_LEGACY_IMAGEUTILS_BACKEND

CRADMIN_LEGACY_IMAGEUTILS_BACKEND
=================================
The string path of a :doc:`cradmin_legacy.imageutils <imageutils>` backend.
Defaults to::

    CRADMIN_LEGACY_IMAGEUTILS_BACKEND = "cradmin_legacy.imageutils.backends.sorl_thumbnail.SorlThumbnail"


.. setting:: CRADMIN_LEGACY_IMAGEUTILS_IMAGETYPE_MAP

CRADMIN_LEGACY_IMAGEUTILS_IMAGETYPE_MAP
=======================================
A map between an *imagetype* (a name you define) and
options for :meth:`cradmin_legacy.imageutils.backends.backendinterface.Interface.transform_image`.

See :doc:`imageutils` for more information.


********************
cradmin_imagearchive
********************


.. setting:: CRADMIN_LEGACY_IMAGEARCHIVE_LISTING_IMAGETYPE

CRADMIN_LEGACY_IMAGEARCHIVE_LISTING_IMAGETYPE
=============================================
The :doc:`imageutils` imagetype that defines how images in the
cradmin listing of archive images in cradmin imagearchive is transformed.
If this is not defined, we default to scaling the image to fit within
a 100x60 px box. If you you change this, you will also want to
change :setting:`.CRADMIN_LEGACY_IMAGEARCHIVE_LISTING_IMAGEWIDTH`


.. setting:: CRADMIN_LEGACY_IMAGEARCHIVE_LISTING_IMAGEWIDTH

CRADMIN_LEGACY_IMAGEARCHIVE_LISTING_IMAGEWIDTH
==============================================
The width of the column containing the image preview in the listing
of archive images in the cradmin view. Defaults to ``100``.


.. setting:: CRADMIN_LEGACY_IMAGEARCHIVE_PREVIEW_IMAGETYPE

CRADMIN_LEGACY_IMAGEARCHIVE_PREVIEW_IMAGETYPE
=============================================
The :doc:`imageutils` imagetype that defines how previews of images
in cradmin imagearchive is transformed. If this is not defined, we default
to scaling the image to fit within a 300x300 px box.


.. setting:: CRADMIN_LEGACY_IMAGEARCHIVE_FILENAMEPATTERN

CRADMIN_LEGACY_IMAGEARCHIVE_FILENAMEPATTERN
===========================================
The pattern to use for the filename for ``cradmin_imagearchive`` images. Defaults
to::

    cradmin_imagearchive_images/{id}-{uuid}{extension}

You can change this if you want to store archive images in another directory.
Any pattern must contain all the variables in the pattern above.


.. setting:: CRADMIN_LEGACY_IMAGEARCHIVE_MAX_FILESIZE

CRADMIN_LEGACY_IMAGEARCHIVE_MAX_FILESIZE
========================================
Max file size for images uploaded to the image archive as a string
compatible with :func:`cradmin_legacy.utils.crhumanize.py.dehumanize_readable_filesize`.

Defaults to ``None``, which means that there is no limit by default. Examples::

    CRADMIN_LEGACY_IMAGEARCHIVE_MAX_FILESIZE = '500KB'
    CRADMIN_LEGACY_IMAGEARCHIVE_MAX_FILESIZE = '10MB'
    CRADMIN_LEGACY_IMAGEARCHIVE_MAX_FILESIZE = '2.5GB'


.. setting:: CRADMIN_LEGACY_SUPERUSERUI_THEME_PATH

CRADMIN_LEGACY_SUPERUSERUI_THEME_PATH
=====================================
The theme path to use by default for ``cradmin_legacy.superuserui``.
Defaults to ``None``, which means that we use :setting:`CRADMIN_LEGACY_THEME_PATH`.
