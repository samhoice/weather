from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView

from .models import Location

# Create your views here.
class LocationCreate(CreateView):
	model = Location
	fields = ['zipcode']
	# success_url = reverse('location:detail')

class LocationDetail(DetailView):
	model = Location
	template = "location/detail.html"