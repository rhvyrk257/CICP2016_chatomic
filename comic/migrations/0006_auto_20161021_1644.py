# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0005_doing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comicinfo',
            old_name='file_name',
            new_name='comic_name',
        ),
        migrations.RemoveField(
            model_name='comicinfo',
            name='path_name',
        ),
        migrations.AddField(
            model_name='comicinfo',
            name='bubble_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]