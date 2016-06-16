# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_whitelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whitelist',
            name='ip',
            field=models.GenericIPAddressField(db_index=True),
        ),
    ]
