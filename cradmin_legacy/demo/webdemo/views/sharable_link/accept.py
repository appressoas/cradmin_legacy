from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect

from django_cradmin.apps.cradmin_invite.baseviews.accept import AbstractAcceptInviteView


class AcceptPublicSiteAdminInviteView(AbstractAcceptInviteView):
    # description_template_name = 'myapp/invite_description.django.html'

    def get_appname(self):
        return 'webdemo_sharable_link'

    def invite_accepted(self, generictoken):
        site = generictoken.content_object
        site.admins.add(self.request.user)
        messages.success(self.request, 'You are now admin on %(site)s' % {'site': site})
        return HttpResponseRedirect(settings.LOGIN_URL)
