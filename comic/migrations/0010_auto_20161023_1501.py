# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0009_auto_20161021_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicinfo',
            name='x1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comicinfo',
            name='x2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comicinfo',
            name='y1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comicinfo',
            name='y2',
            field=models.FloatField(default=0),
        ),
    ]
