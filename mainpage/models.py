from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
	user_name = models.CharField(max_length=200)
	grade = models.CharField(max_length=200)

	def __str__(self):
		return self.user_name
	def return_user_name(self):
		return self.user_name

class Devices(models.Model):
	device_name = models.CharField(max_length=200)
	ip = models.CharField(max_length=20)
	is_attestated = models.BooleanField(default=False)
	attestated_time = models.DateTimeField('date published', null=True)
	user = models.ForeignKey(Users)

	def __str__(self):
		return self.device_name
	def return_device_name(self):
		return self.device_name

