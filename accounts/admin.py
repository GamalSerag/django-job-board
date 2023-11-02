from django.contrib import admin
from setuptools.command.register import register

from .models import Profile, City
# Register your models here.

admin.site.register(Profile)
admin.site.register(City)