# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 20:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titles',
            new_name='title',
        ),
    ]
