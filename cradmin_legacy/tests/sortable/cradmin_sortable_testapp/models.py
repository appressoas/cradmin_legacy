"""
An example app using Sortable.
"""
from __future__ import unicode_literals
from django.db import models
from future.utils import python_2_unicode_compatible
from cradmin_legacy.sortable.models import SortableBase
from cradmin_legacy.sortable.models import SortableManagerBase


@python_2_unicode_compatible
class ItemContainer(models.Model):
    """
    A test class for being a container for items that should be sorted.

    It has a name field only for testing purposes.
    """
    name = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        default='')

    def __str__(self):
        return 'Item container {}, {}'.format(self.id, self.name)


class SortableItemManager(SortableManagerBase):
    """
    Sortable items that inherit SortableBase must also have a manager that inherits SortableManagerBase.

    The `parent_attribute` must be set, and it must have the name of the parent in which the items belong.
    """
    parent_attribute = 'container'


class SortableItem(SortableBase):
    """
    The sortable item. The important thing here is the usage og SortableItemManager.

    The `sort_index` field is inherited from SortableBase.
    """
    container = models.ForeignKey(ItemContainer, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        default='')
    objects = SortableItemManager()

    def __str__(self):
        return 'Id: {}, Sort index: {}, Name: {}, {}'.format(
            self.id,
            self.sort_index,
            self.name,
            self.container
        )
