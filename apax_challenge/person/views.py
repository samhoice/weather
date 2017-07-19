from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from .models import Person

class PersonView(DetailView):
	model = Person
	template_name = 'person/detail.html'