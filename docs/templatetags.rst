#############
Template tags
#############


*******************
cradmin_legacy_tags
*******************

.. currentmodule:: cradmin_legacy.templatetags.cradmin_legacy_tags
.. automodule:: cradmin_legacy.templatetags.cradmin_legacy_tags


.. _cradmin_legacy_icon_tags:

************************
cradmin_legacy_icon_tags
************************

The ``cradmin_legacy_icon_tags`` Django template tag library defines tags that makes
it easy to swap out the icons used by the provided Django cradmin components.

It is used like this:

.. code-block:: htmldjango

    {% load cradmin_legacy_icon_tags %}

    <span class="{% cradmin_icon 'search' %}"></span>

where ``{% cradmin_icon 'search' %}`` will look up css classes for the
icon in the ``CRADMIN_LEGACY_CSS_ICON_MAP`` Django setting.
If ``CRADMIN_LEGACY_CSS_ICON_MAP`` is not set, we default to
:obj:`.cradmin_legacy.css_icon_map.FONT_AWESOME`, but you can
easily provide your own with something like this in your settings.py::

    from cradmin_legacy import css_icon_map
    CRADMIN_LEGACY_CSS_ICON_MAP = css_icon_map.FONT_AWESOME.copy()
    CRADMIN_LEGACY_CSS_ICON_MAP.update({
        'search': 'my my-search-icon'
    })

You can even add your own icons and use ``cradmin_icon`` for your own
views/components.


.. currentmodule:: cradmin_legacy.css_icon_map
.. automodule:: cradmin_legacy.css_icon_map


*************************
cradmin_legacy_image_tags
*************************
See :doc:`imageutils` for examples.and details.

.. currentmodule:: cradmin_legacy.templatetags.cradmin_legacy_image_tags
.. automodule:: cradmin_legacy.templatetags.cradmin_legacy_image_tags


*************************
cradmin_legacy_email_tags
*************************
See :doc:`apps.cradmin_email`.
