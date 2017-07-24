from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, FormView
from django.views import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Person

class PersonHome(View):
	""" Kind of a crude redirect to the login page. SHould just rewrite URLs I guess """
	def get(self, request):
		if request.user.is_authenticated:
			user = request.user.pk
			person = get_object_or_404(Person, user=user)
			return HttpResponseRedirect(reverse('person:detail', kwargs={'pk': person.pk}))
		else:
			return HttpResponseRedirect(reverse('person:login'))

class PersonView(DetailView):
	""" Shows us a person page """
	model = Person
	template_name = 'person/detail.html'

class PersonForm(forms.Form):
	""" New user and login form """
	name = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def clean_name(self):
		""" No duplicates """
		field = self.cleaned_data['name']
		if User.objects.filter(username=field):
			raise forms.ValidationError('Name is in use')

		return field

class PersonCreate(FormView):
	""" Create a user """
	form_class = PersonForm
	template_name = "person/create.html"
	success_url = '/'

	def form_valid(self, form):
		""" Create a user and link it to a new Person"""
		username = form.cleaned_data['name']
		pw = form.cleaned_data['password']

		user = User.objects.create_user(username, password=pw)
		if user:
			login(self.request, user)

		p = Person(user=user)
		p.save()
		return super(PersonCreate, self).form_valid(form)