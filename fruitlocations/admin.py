from django.contrib import admin
from django.contrib.gis import admin
from .models import FruitLocate

# Register your models here.
admin.site.register(FruitLocate, admin.OSMGeoAdmin)

