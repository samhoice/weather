# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20170721_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='location',
            name='lon',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
    ]
