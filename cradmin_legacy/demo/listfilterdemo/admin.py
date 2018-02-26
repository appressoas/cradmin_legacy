from __future__ import unicode_literals
from django.contrib import admin
from django_cradmin.demo.listfilterdemo.models import Site, Person


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'admins_as_string')

    def admins_as_string(self, obj):
        return ', '.join([user.username for user in obj.admins.all()])
    admins_as_string.short_description = "Admins"

admin.site.register(Site, SiteAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'site',
        'banned_datetime',
    ]

    def get_queryset(self, request):
        return super(PersonAdmin, self).get_queryset(request)\
            .select_related('site')

admin.site.register(Person, PersonAdmin)
