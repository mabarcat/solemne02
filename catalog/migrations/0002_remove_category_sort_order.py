# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-08 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sort_order',
        ),
    ]
