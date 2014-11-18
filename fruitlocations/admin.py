from django.contrib import admin
from django.contrib.gis import admin
from .models import FruitLocations

# Register your models here.
admin.site.register(FruitLocations, admin.OSMGeoAdmin)

