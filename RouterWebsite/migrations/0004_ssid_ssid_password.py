# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RouterWebsite', '0003_ssid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssid',
            name='ssid_password',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
