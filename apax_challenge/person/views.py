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
	def get(self, request):
		if request.user.is_authenticated:
			user = request.user.pk
			person = get_object_or_404(Person, user=user)
			return HttpResponseRedirect(reverse('person:detail', kwargs={'pk': person.pk}))
		else:
			return HttpResponseRedirect(reverse('person:login'))

class PersonView(DetailView):
	model = Person
	template_name = 'person/detail.html'

class PersonForm(forms.Form):
	name = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class PersonCreate(FormView):
	form_class = PersonForm
	template_name = "person/create.html"
	success_url = '/'

	def form_valid(self, form):

		username = form.cleaned_data['name']
		pw = form.cleaned_data['password']

		user = User.objects.create_user(username, password=pw)
		if user:
			login(self.request, user)

		p = Person(user=user)
		p.save()
		return super(PersonCreate, self).form_valid(form)