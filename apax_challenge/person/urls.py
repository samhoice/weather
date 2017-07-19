from django.conf.urls import url

from django.views.generic import TemplateView
from .views import PersonView

urlpatterns = [
	url(r'home', TemplateView.as_view(template_name="person/home.html")),
	url(r'^d/(?P<pk>\d+)[/]', PersonView.as_view(), name = "detail")
]