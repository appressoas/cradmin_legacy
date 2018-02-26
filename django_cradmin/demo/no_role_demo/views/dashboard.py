from __future__ import unicode_literals
from django.views.generic import TemplateView

from django_cradmin import crapp


class DashboardView(TemplateView):
    template_name = 'no_role_demo/dashboard.django.html'


class App(crapp.App):
    appurls = [
        crapp.Url(r'^$', DashboardView.as_view(), name=crapp.INDEXVIEW_NAME)
    ]
