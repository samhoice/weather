from django.db import models

# Create your models here.
class Location(models.Model):
	zipcode = models.CharField(max_length=5)

	def __str__(self):
		return "{}".format(self.zipcode)