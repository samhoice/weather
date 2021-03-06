# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='detailed_forcast',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='location',
            name='high',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='low',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='short_forecast',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='wind_dir',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='location',
            name='wind_speed',
            field=models.IntegerField(default=0),
        ),
    ]
