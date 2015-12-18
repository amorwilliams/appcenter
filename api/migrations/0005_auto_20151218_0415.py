# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151218_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='status',
            field=models.IntegerField(choices=[(1, 'Normal'), (2, 'Busy'), (3, 'Full'), (0, 'Stop')], default=0),
        ),
    ]
