from django.conf.urls import url

from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView
from .views import PersonView, PersonHome, PersonCreate

urlpatterns = [
	url(r'home',
		PersonHome.as_view(),
		name='home'),
	url(r'^(?P<pk>\d+)[/]',
		PersonView.as_view(),
		name="detail"),

	url(r'^login',
		auth_views.login,
		{'template_name': 'person/login.html'},
		name='login'),
	url(r'^logout',
		auth_views.logout,
		{'next_page': reverse_lazy('person:login')},
		name='logout'),

	url(r'^create',
		PersonCreate.as_view(),
		name="create")
]