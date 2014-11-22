from django.contrib import admin
from django.contrib.gis import admin as geo_admin
from .models import FruitLocations

# Register your models here.
admin.site.register(FruitLocations, geo_admin.OSMGeoAdmin)

