# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0002_auto_20161014_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicinfo',
            name='pn',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]
