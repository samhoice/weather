from django.db import models

from django.core.urlresolvers import reverse

class Location(models.Model):
	""" The could (should?) be broken into two, to separate the weather
	data. This is easy, and since this is the end of this project...

	Save the location information and don't load it twice

	Save the most recent weather data, and when we loaded it in case we
	want to cache it

	"""
	zipcode = models.CharField(max_length=5)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=128)

	lat = models.DecimalField(default=0.0, max_digits=6, decimal_places=3)
	lon = models.DecimalField(default=0.0, max_digits=6, decimal_places=3)

	high = models.IntegerField(default=0)
	low = models.IntegerField(default=0)

	wind_speed = models.IntegerField(default=0)
	wind_dir = models.CharField(max_length=3, default="")

	short_forecast = models.TextField(default="")
	detailed_forecast = models.TextField(default="")

	last_update = models.DateTimeField(null=True)

	def __str__(self):
		return "{}".format(self.zipcode)

	def get_absolute_url(self):
		return reverse('location:detail', kwargs={'pk': self.pk})