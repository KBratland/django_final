# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruitlocations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitlocations',
            name='fruit_variety',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
