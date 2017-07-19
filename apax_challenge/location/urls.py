from django.conf.urls import url

from .views import LocationCreate, LocationDetail

urlpatterns = [
	url(r'^n[/]$', LocationCreate.as_view(), name = "create"),
	url(r'^(?P<pk>\d+)[/]', LocationDetail.as_view(), name = "detail"),
]