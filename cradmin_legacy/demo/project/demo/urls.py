from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views import static

from cradmin_legacy.demo.listfilterdemo.cradmin import ListfilterDemoCrAdminInstance
from cradmin_legacy.demo.login_not_required_demo.cradmin import LoginNotRequiredCrAdminInstance
from cradmin_legacy.demo.multiselect2demo.cradmin import MultiselectDemoCrAdminInstance
from cradmin_legacy.demo.no_role_demo.cradmin import NoRoleCrAdminInstance
from cradmin_legacy.demo.project.demo.views.demo_overview import DemoView
from cradmin_legacy.demo.usermanagerdemo.cradmin import UsermanagerCrAdminInstance
from cradmin_legacy.demo.webdemo.cradmin import WebdemoCrAdminInstance
from cradmin_legacy.superuserui import superuserui_registry


urlpatterns = [
    url(r'^authenticate/', include('cradmin_legacy.apps.cradmin_authenticate.urls')),
    url(r'^resetpassword/', include('cradmin_legacy.apps.cradmin_resetpassword.urls')),
    url(r'^activate_account/', include('cradmin_legacy.apps.cradmin_activate_account.urls')),
    url(r'^register/', include('cradmin_legacy.apps.cradmin_register_account.urls')),

    url(r'^djangoadmin/', include(admin.site.urls)),
    url(r'^webdemo/', include(WebdemoCrAdminInstance.urls())),
    url(r'^listfilterdemo/', include(ListfilterDemoCrAdminInstance.urls())),
    url(r'^multiselect2demo/', include(MultiselectDemoCrAdminInstance.urls())),
    url(r'^login_not_required_demo/', include(LoginNotRequiredCrAdminInstance.urls())),
    url(r'^no_role_demo/', include(NoRoleCrAdminInstance.urls())),
    url(r'^webdemo/', include('cradmin_legacy.demo.webdemo.urls')),
    url(r'^usermanagerdemo/', include(UsermanagerCrAdminInstance.urls())),
    url(r'^cradmin_temporaryfileuploadstore/', include('cradmin_legacy.apps.cradmin_temporaryfileuploadstore.urls')),
    url(r'^$', DemoView.as_view()),
    url(r'^media/(?P<path>.*)$', static.serve, {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^polls/', include('cradmin_legacy.demo.polls_demo.urls')),

    url(r'^superuser/', include(superuserui_registry.default.make_cradmin_instance_class().urls())),
]
