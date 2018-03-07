from django.conf.urls import include, url

from cradmin_legacy.demo.usermanagerdemo.cradmin import UsermanagerCrAdminInstance
from cradmin_legacy.demo.webdemo.cradmin import WebdemoCrAdminInstance

urlpatterns = [
    url(r'^cradmin_authenticate/', include('cradmin_legacy.apps.cradmin_authenticate.urls')),
    url(r'^cradmin_temporaryfileuploadstore/', include('cradmin_legacy.apps.cradmin_temporaryfileuploadstore.urls')),
    url(r'^cradmin_resetpassword/', include('cradmin_legacy.apps.cradmin_resetpassword.urls')),
    url(r'^cradmin_activate_account/', include('cradmin_legacy.apps.cradmin_activate_account.urls')),
    url(r'^cradmin_register_account/', include('cradmin_legacy.apps.cradmin_register_account.urls')),

    # Demo apps
    url(r'^webdemoadmin/', include(WebdemoCrAdminInstance.urls())),
    url(r'^webdemo/', include('cradmin_legacy.demo.webdemo.urls')),
    url(r'^usermanagerdemo/', include(UsermanagerCrAdminInstance.urls())),
]
