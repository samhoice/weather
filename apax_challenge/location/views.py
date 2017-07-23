from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Location
from person.models import Person
from .helpers import get_weather

import requests
import json
from django.utils import timezone
from datetime import timedelta


# Create your views here.
class LocationCreate(LoginRequiredMixin, CreateView):
	model = Location
	fields = ['zipcode']

	def form_valid(self, form):
		try:
			# try not to add locations more than once
			loc = Location.objects.get(zipcode = form.cleaned_data['zipcode'])
		except Location.DoesNotExist:
			# ok, create one
			loc = form.save(False)

			# http://maps.googleapis.com/maps/api/geocode/json?address=40383
			zip_url = "http://maps.googleapis.com/maps/api/geocode/json?address={}".format(loc.zipcode)
			location_json = requests.get(zip_url)

			location_struct = json.loads(location_json.text)
			# status: ok
			for addy_comp in location_struct['results'][0]['address_components']:
				if addy_comp['types'][0] == 'administrative_area_level_1':
					loc.state = addy_comp['short_name']
				elif addy_comp['types'][0] == 'locality':
					loc.city = addy_comp['short_name']

			loc.lat = location_struct['results'][0]['geometry']['location']['lat']
			loc.lon = location_struct['results'][0]['geometry']['location']['lng']

			loc.save()

		person = self.request.user.person
		person.location.add(loc)

		return HttpResponseRedirect(reverse('person:detail', kwargs={'pk': person.pk}))


class LocationDetail(DetailView):
	model = Location
	template = "location/detail.html"

	def get_context_data(self, **kwargs):
		context = super(LocationDetail, self).get_context_data(**kwargs)

		if(not context['object'].last_update or
			timezone.now() - context['object'].last_update > timedelta(0, 300)):
			weather_dict = get_weather(context['object'].lat, context['object'].lon)
			context['object'].high = weather_dict['high']
			context['object'].low = weather_dict['low']

			# context['object'].wind_speed = weather_dict['wind_speed']

			context['object'].short_forecast = weather_dict['short_forecast']
			context['object'].detailed_forecast = weather_dict['detailed_forecast']

			context['object'].last_update = timezone.now()

			context['object'].save()

		return context


class LocationRefresh(View):
	def get(self, request, pk):
		loc = get_object_or_404(Location, pk=pk)
		weather_dict = get_weather(loc.lat, loc.lon)
		loc.high = weather_dict['high']
		loc.low = weather_dict['low']
		loc.short_forecast = weather_dict['short_forecast']
		loc.detailed_forecast = weather_dict['detailed_forecast']
		loc.last_update = timezone.now()
		loc.save()

		return HttpResponseRedirect(reverse('home'))

class LocationRefreshAll(View):
	def get(self, request):
		person = request.user.person

		location_list = person.location.all()
		for loc in location_list:
			weather_dict = get_weather(loc.lat, loc.lon)
			loc.high = weather_dict['high']
			loc.low = weather_dict['low']
			loc.short_forecast = weather_dict['short_forecast']
			loc.detailed_forecast = weather_dict['detailed_forecast']
			loc.last_update = timezone.now()
			loc.save()

		return HttpResponseRedirect(reverse('home'))