# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=125)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.BigIntegerField()),
                ('modelo', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('sexo', models.CharField(default='M', max_length=1)),
            ],
        ),
    ]
