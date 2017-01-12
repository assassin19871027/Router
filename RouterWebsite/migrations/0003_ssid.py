# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RouterWebsite', '0002_traffic'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssid_name', models.CharField(max_length=100)),
                ('ssid_network', models.CharField(max_length=20)),
                ('ssid_type', models.BooleanField(default=True)),
                ('ssid_active', models.BooleanField(default=True)),
                ('ssid_guest', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
