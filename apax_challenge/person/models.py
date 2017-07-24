from django.db import models
from django.contrib.auth.models import User

from location.models import Location

class Person(models.Model):
	""" Very simple person model """
	user = models.OneToOneField(User)
	location = models.ManyToManyField(Location)

	def __str__(self):
		return self.user.username