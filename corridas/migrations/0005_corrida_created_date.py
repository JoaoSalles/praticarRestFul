# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corridas', '0004_corrida'),
    ]

    operations = [
        migrations.AddField(
            model_name='corrida',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
