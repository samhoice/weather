from django.db import models
from django.contrib.auth.models import User

from location.models import Location

# Create your models here.
class Person(models.Model):
	user = models.OneToOneField(User)
	location = models.ManyToManyField(Location)

	def __str__(self):
		return self.user.username