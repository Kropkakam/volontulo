# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-13 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volontulo', '0014_auto_20180610_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='action_status',
        ),
    ]
