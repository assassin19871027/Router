# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RouterWebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100)),
                ('bandwidth', models.DecimalField(max_digits=10, decimal_places=0)),
                ('time', models.DecimalField(max_digits=10, decimal_places=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
