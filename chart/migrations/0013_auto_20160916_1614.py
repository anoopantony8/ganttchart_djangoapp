# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0012_task_depends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
