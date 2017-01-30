# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-07 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0006_remove_task_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='can_write',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='can_write_on_parent',
            field=models.BooleanField(default=False),
        ),
    ]