######################################
`sortable` --- Making objects sortable
######################################

To make a model sortable, you need the following two additions to your model:

#. You need to inherit from :class:`.SortableBase` (an abstract model) instead of ``django.db.Model``,
#. You need to create a subclass of :class:`.SortableManagerBase` and attach that subclass
   as a manager for your model.

Example::

    from cradmin_legacy.sortable.models import SortableBase
    from cradmin_legacy.sortable.models import SortableManagerBase

    class MySortableItemManager(SortableManagerBase):
        parent_attribute = 'container'

    class MySortableItem(SortableBase):
        container = models.ForeignKey(ItemContainer, blank=False, null=False)
        name = models.CharField(...)

        objects = MySortableItemManager()

The class that inherits ``SortableBase`` gets an attribute ``sort_index``. If you want the default ordering
for this model to be this attribute, you should add the following meta option on the model::

    class Meta:
        ordering = ['sort_index']



*****************************
Custom QuerySet with sortable
*****************************

If you want to use a custom queryset with SortableBase, you need to extend
:class:`cradmin_legacy.sortable.models.SortableQuerySetBase`. Example::

    from cradmin_legacy.sortable.models import SortableBase
    from cradmin_legacy.sortable.models import SortableManagerBase
    from cradmin_legacy.sortable.models import SortableQuerySetBase

    class MySortableItemQuerySet(SortableQuerySetBase):
        def my_queryset_method(self):
            pass

    class MySortableItemManager(SortableManagerBase):
        parent_attribute = 'container'

        def get_query_set(self):
            return MySortableItemQuerySet(self.model, using=self._db)

    class MySortableItem(SortableBase):
        container = models.ForeignKey(ItemContainer, blank=False, null=False)
        name = models.CharField(...)

        objects = MySortableItemManager()



***********
How to sort
***********

Sorting is done by using these methods:

- :meth:`cradmin_legacy.sortable.models.SortableManagerBase.sort_before`
- :meth:`cradmin_legacy.sortable.models.SortableManagerBase.sort_last`
- :meth:`cradmin_legacy.sortable.models.SortableManagerBase.set_newitem_sort_index_to_last`

Example::

    # Make a new item and put it last in the list
    myitem = MySortableItem(container=somecontainer, name='Some name')
    MySortableItem.objects.set_newitem_sort_index_to_last(myitem)
    myitem.save()

    # Move the given item before the item with id 777
    # NOTE: Unlike set_newitem_sort_index_to_last(), sort_before() and sort_last()
    #       saves the item.
    MySortableItem.objects.sort_before(someitem, sort_before_id=777)

    # Move the given item last in the list
    MySortableItem.objects.sort_last(someitem)
    # ... or ...
    MySortableItem.objects.sort_before(someitem, sort_before_id=None)


**************************************************************
Makin an Admin UI that automatically adds items last in parent
**************************************************************
Making an Admin UI that automatically adds items last in parent is easy. Just extend
:class:`cradmin_legacy.sortable.admin.SortableModelAdmin` instead of
``django.contrib.admin.ModelAdmin``::

    from cradmin_legacy.sortable.admin import SortableModelAdmin

    class MySortableItemAdmin(SortableModelAdmin):
        pass

    admin.site.register(models.MySortableItem, MySortableItemAdmin)

You may also want to show the sort order by default in the admin UI listing,
with something like this::

    class MySortableItemAdmin(SortableModelAdmin):
        ordering = ['container__name', 'sort_index']


***
API
***

.. autoclass:: cradmin_legacy.sortable.models.SortableQuerySetBase
    :members:

.. autoclass:: cradmin_legacy.sortable.models.SortableManagerBase
    :members:

.. autoclass:: cradmin_legacy.sortable.models.SortableBase
    :members:

.. autoclass:: cradmin_legacy.sortable.admin.SortableModelAdmin
    :members:
