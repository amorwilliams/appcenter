# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151217_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='api.ChannelInfo'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='api.GameInfo'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='sdk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='api.SDKInfo'),
        ),
    ]
