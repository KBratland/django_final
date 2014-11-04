# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='user_role',
            field=models.CharField(default='Finder', max_length=5, choices=[(b'Finder', b'Finder'), (b'Owner', b'Owner'), (b'Both', b'Both')]),
            preserve_default=False,
        ),
    ]
