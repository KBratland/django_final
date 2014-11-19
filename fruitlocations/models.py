from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis import admin

# Create your models here.


class FruitLocations (models.Model):

    # make choices be the drop down field from fallen fruit

    geom = models.PointField(srid=4326)
    fruit_variety = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.fruit_variety
