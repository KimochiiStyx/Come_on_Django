# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import Company, Person

admin.site.register(Company)
admin.site.register(Person)