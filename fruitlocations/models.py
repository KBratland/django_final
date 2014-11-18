from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis import admin

# Create your models here.


class FruitLocations (models.Model):

    geom = models.PointField(srid=4326)
    fruit_variety = models.CharField("What kind of fruit is it (e.g. apple or pear, but do not include variety)?", max_length=50)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.fruit_variety
