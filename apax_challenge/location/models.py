from django.db import models

from django.core.urlresolvers import reverse

class Location(models.Model):
	zipcode = models.CharField(max_length=5)

	def __str__(self):
		return "{}".format(self.zipcode)

	def get_absolute_url(self):
		return reverse('location:detail', kwargs={'pk': self.pk})