# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruitLocations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('fruit_variety', models.CharField(max_length=50, verbose_name=b'What kind of fruit is it (e.g. apple or pear, but do not include variety)?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
