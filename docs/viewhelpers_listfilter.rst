############################################################
`viewhelpers.listfilter` --- a framework for filtering lists
############################################################

The ``cradmin_legacy.viewhelpers.listfilter`` framework makes it
easy to add filters to your listviews. It works with any view that
lists items (from the database or other sources).


********************************
Getting started with listbuilder
********************************
In this example we will create a full example using :doc:`listbuilder <viewhelpers_listbuilder>`.
We will skip all the role-related stuff.


Create the models
=================
Create the following model in your models.py:

.. literalinclude:: /../cradmin_legacy/demo/listfilterdemo/models.py

.. note::

    The ``@python_2_unicode_compatible`` is just there to make the model
    compatible with both python 2 and 3.


Create the view
===============

Create a ``views`` module in your app, and add ``views/personlist.py``
with the following code (adjust the imports for your app):

.. literalinclude:: /../cradmin_legacy/demo/listfilterdemo/views/personlist.py

We add the filters in the ``add_filterlist_items()``-method.
We add three filters:

- Search by ``name``.
  Uses :class:`~cradmin_legacy.viewhelpers.listfilter.django.single.textinput.Search`.
- Filter by ``banned_datetime``.
  Uses :class:`~cradmin_legacy.viewhelpers.listfilter.django.single.select.NullDateTime`.
- Order by name (descending and ascending). This is defined
  using a class. Some of the provided base classes for filters
  work like this because they need something that can not be
  easily/cleanly defined using parameters.
  Uses :class:`~cradmin_legacy.viewhelpers.listfilter.django.single.select.AbstractOrderBy`.

The ``get_filterlist_url()``-method is required. Refer to
:meth:`~cradmin_legacy.viewhelpers.listfilter.listfilter_viewmixin.ViewMixin.get_filterlist_url`
for more details on this method.

The ``get_queryset_for_role``-method is just like it would be for
any listbuildeview except that we add a single line to allow
the filterlist to filter the queryset.


Create a cradmin instance
=========================
Add a ``cradmin.py`` to your app with the following code (adjust the imports for your app):

.. literalinclude:: /../cradmin_legacy/demo/listfilterdemo/cradmin.py


Add to urls.py
==============
Add something like this to you ``urls.py``::

    url(r'^listfilterdemo/', include(ListfilterDemoCrAdminInstance.urls())),


Try it out
==========
Start up your django development server, and visit the app at the URL you added to your ``urls.py``.

You will have to use the shell to create at least one ``Site`` and one ``Person``.


Full source code
================
See :github_folder:`cradmin_legacy/demo/listfilterdemo`.


************************************
Getting started with ObjectTableView
************************************
Works just like the listbuilder example above, but you use
``objecttable.FilterListMixin, objecttable.ObjectTableView`` instead of
``listbuilderview.FilterListMixin, listbuilderview.View`` in the view.


***************
Advanced topics
***************

Hide labels
===========
You have two options:

- Override :meth:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilter.AbstractFilter.get_label_is_screenreader_only`
  on the filters you want to hide the values for.
- Override :meth:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist.AbstractFilterList.get_label_is_screenreader_only_by_default`.
  In views inheriting from :class:`cradmin_legacy.viewhelpers.listfilter.listfilter_viewmixin.ViewMixin`
  (like the getting started example above), you can override
  :meth:`~cradmin_legacy.viewhelpers.listfilter.listfilter_viewmixin.ViewMixin.get_label_is_screenreader_only_by_default`
  to achive the same effect.

Test filtering with slow requests
=================================
To test how the filters behave with slow requests, use :doc:`delay_middleware`.


Share data between your filters
===============================
If you want to share data between all of your filtes (such as aqueryset),
you can override one of the AbstractFilterList subclasses
and send the queryset into ``__init__()``. All of the
filters (and other :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild.AbstractFilterListChild`)
has access to the filterlist via their ``filterlist`` attribute.
This can of course be used to share any kind of information that your
filters need.


Use an existing AbstractRenderableWithCss
=========================================
If you have an :class:`~cradmin_legacy.renderable.AbstractRenderableWithCss`
that you want to use in a filterlist, you can just mix in the
:class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild.FilterListChildMixin`
class. Example::

    from cradmin_legacy import renderable
    from cradmin_legacy.viewhelpers import listfilter
    from cradmin_legacy.viewhelpers.listfilter.base import abstractfilterlistchild

    class MyRendereable(renderable.AbstractRenderableWithCss):
        """
        ...
        """

    class MyRenderableFilterListChild(MyRendereable,
                                      abstractfilterlistchild.FilterListChildMixin):
        pass

    filterlist = listfilter.lists.Vertical(...)
    filterlist.append(MyRenderableFilterListChild())

**********************
Design --- why and how
**********************
The listfilter module is designed to be data store agnostic. This
means that we use general purpose terms and logic that does not
bind the framework to a specific data storage backend.

The most obvious of these strange terms when working with the filters in
``cradmin_legacy.viewshelpers.listbuilder.django`` is that you
send the model field into the filter via the ``slug`` parameter.
This is much easier to understand when you know the following:

- Each filter has a slug. The slug is the thing added to the URL,
  and reversed to extract the filter values from the URL.
- The base class for all Django filters,
  :class:`~cradmin_legacy.viewhelpers.listfilter.django.base.DjangoOrmFilterMixin`,
  defines :meth:`~cradmin_legacy.viewhelpers.listfilter.django.base.DjangoOrmFilterMixin.get_modelfield`,
  which simply defalts to returning the slug of the filter. You can override this if you want
  to have a different slug in the URL than the model field name.


Code structure
==============
The code is organized into these sub-modules of ``cradmin_legacy.viewhelpers.listfilter``:

    base
        Base classes. Very rarely used directly except when creating completely custom
        components for the framework.
    lists
        Re-usable subclasses of
        :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist.AbstractFilterList`.
    basefilters
        Re-usable data store agnostic abstract filter classes.
    django
        Re-usable Django ORM specific subclasses of
        :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilter.AbstractFilter`.
        These are mostly fairly small extensions of classes in ``basefilters`` that just
        add the Django ORM specific stuff.


************
How it works
************
A filter is just a class that lets the user select from a
list of choices and filter a list based on their selection.

The base class (:class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilter.AbstractFilter`)
is completely decoupled from the storage backend, and just provides
methods that any filter needs to override.

A filter is rendered by a :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist.AbstractFilterList`.
A filterlist is simply a list of :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild.AbstractFilterListChild`,
which is a subclass of :class:`~cradmin_legacy.renderable.AbstractRenderableWithCss`.

:class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild.AbstractFilterListChild` can render anything,
so it is perfect for adding things like sectioning and extra text in your
filterlists. For the actual filters, we have :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilter.AbstractFilter`
(a subclass of :class:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild.AbstractFilterListChild`). Subclasses of
this is this gets special treatment by :meth:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist.AbstractFilterList`.


To summarize, you do the following to define filters for a view:

- Create an instance of a subclass of :class:`cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist.AbstractFilterList`.
- Add subclasses of :class:`cradmin_legacy.viewhelpers.listfilter.base.abstractfilter.AbstractFilter` to the filter filterlist.
- Call the render() method of the filter filterlist to render all the filters.


URLs generated by filters
=========================

.. todo:: Change this to talk about FiltersHandler

Each filter has a slug (:meth:`~cradmin_legacy.viewhelpers.listfilter.base.abstractfilter.AbstractFilter.get_slug`).
The slug is used in the URL to identify the filter. Example::

    /my/view/hasimage-true/size-large/tags-a,b/

Here ``tag`` and ``hasimage`` are slugs for the applied filters.

Filters are added to the url with something like ``(?P<filters_string>.*)``.



******************
Django filters API
******************


Singlevalue widgets
===================

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.django.single.select
.. automodule:: cradmin_legacy.viewhelpers.listfilter.django.single.select

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.django.single.textinput
.. automodule:: cradmin_legacy.viewhelpers.listfilter.django.single.textinput


Multivalue widgets
==================

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.django.multi.checkbox
.. automodule:: cradmin_legacy.viewhelpers.listfilter.django.multi.checkbox


Base classes for Django ORM filters
===================================

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.django.base
.. automodule:: cradmin_legacy.viewhelpers.listfilter.django.base



**********************************
Re-usable base classes for filters
**********************************
The following are datastore agnostic abstract base classes for filters.
They deal with rendering, leaving the filtering logic up to
subclasses.

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.basefilters.single.abstractselect
.. automodule:: cradmin_legacy.viewhelpers.listfilter.basefilters.single.abstractselect

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.basefilters.single.abstracttextinput
.. automodule:: cradmin_legacy.viewhelpers.listfilter.basefilters.single.abstracttextinput

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.basefilters.multi.abstractcheckbox
.. automodule:: cradmin_legacy.viewhelpers.listfilter.basefilters.multi.abstractcheckbox


.. _listfilter_lists:

************
Filter lists
************

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.lists
.. automodule:: cradmin_legacy.viewhelpers.listfilter.lists


***********
View mixins
***********

For listbuilder views
=====================
:class:`cradmin_legacy.viewhelpers.listbuilderview.FilterListMixin`

For ObjectTableView
===================
:class:`cradmin_legacy.viewhelpers.objecttable.FilterListMixin`


Custom views
============
If you are not using objecttable or listbuilder, you can use
:class:`cradmin_legacy.viewhelpers.listfilter.listfilter_viewmixin.ViewMixin`.

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.listfilter_viewmixin
.. automodule:: cradmin_legacy.viewhelpers.listfilter.listfilter_viewmixin


********
Base API
********

.. note::

  You do not use the ``cradmin_legacy.viewhelpers.listfilter.base``
  API directly - You can use the classes as superclasses when you
  create custom filters or filterlists.

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.base.abstractfilter
.. automodule:: cradmin_legacy.viewhelpers.listfilter.base.abstractfilter

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild
.. automodule:: cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlistchild

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist
.. automodule:: cradmin_legacy.viewhelpers.listfilter.base.abstractfilterlist

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.base.exceptions
.. automodule:: cradmin_legacy.viewhelpers.listfilter.base.exceptions

.. currentmodule:: cradmin_legacy.viewhelpers.listfilter.base.filtershandler
.. automodule:: cradmin_legacy.viewhelpers.listfilter.base.filtershandler
