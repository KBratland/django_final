# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('user_role', models.CharField(max_length=6, choices=[(b'Finder', b'Finder'), (b'Owner', b'Owner'), (b'Both', b'Both')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
