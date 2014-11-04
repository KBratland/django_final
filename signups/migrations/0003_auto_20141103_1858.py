# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_signup_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='user_role',
            field=models.CharField(max_length=6, choices=[(b'Finder', b'Finder'), (b'Owner', b'Owner'), (b'Both', b'Both')]),
            preserve_default=True,
        ),
    ]
