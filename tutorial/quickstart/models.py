# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=45)
	address = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=45)
	phone = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name