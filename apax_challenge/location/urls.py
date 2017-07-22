from django.conf.urls import url

from .views import LocationCreate, LocationDetail, LocationRefresh

urlpatterns = [
	url(r'^n[/]$', LocationCreate.as_view(), name = "create"),
	url(r'^(?P<pk>\d+)[/]', LocationDetail.as_view(), name = "detail"),
	url(r'^r/(?P<pk>\d+)[/]', LocationRefresh.as_view(), name="refresh"),
]