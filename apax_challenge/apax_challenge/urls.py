"""apax_challenge URL Configuration

So, person doesn't really do much, but it and location get their own
namespaces. See location.urls and person.urls for more
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/',
        admin.site.urls),
    url(r'^p/',
        include('person.urls', namespace="person")),
    url(r'^l/',
        include('location.urls', namespace="location")),
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('person:home')),
        name="home"),
]
