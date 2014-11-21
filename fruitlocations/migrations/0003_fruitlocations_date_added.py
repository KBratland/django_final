# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fruitlocations', '0002_auto_20141118_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitlocations',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 18, 22, 40, 34, 409506, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
