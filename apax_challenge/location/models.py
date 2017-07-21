from django.db import models

from django.core.urlresolvers import reverse

class Location(models.Model):
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
	detailed_forcast = models.TextField(default="")

	def __str__(self):
		return "{}".format(self.zipcode)

	def get_absolute_url(self):
		return reverse('location:detail', kwargs={'pk': self.pk})