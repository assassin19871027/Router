# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('domain', models.IPAddressField()),
                ('activity', models.BooleanField(default=True)),
                ('visited', models.BooleanField(default=False)),
                ('visited_number', models.DecimalField(max_digits=10, decimal_places=0)),
                ('bandwidth_usage', models.DecimalField(max_digits=2, decimal_places=0)),
                ('compliance', models.BooleanField(default=True)),
                ('priority', models.BooleanField(default=False)),
                ('block', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-visited_number'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('dev', models.ForeignKey(to='RouterWebsite.Device')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='device',
            name='user_rule',
            field=models.ForeignKey(to='RouterWebsite.Rule'),
            preserve_default=True,
        ),
    ]
