# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0004_auto_20161020_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('path_name', models.CharField(max_length=200)),
                ('flag', models.IntegerField(default=0)),
            ],
        ),
    ]
