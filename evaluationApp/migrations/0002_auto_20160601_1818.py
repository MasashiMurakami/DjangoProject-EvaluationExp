# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation201606',
            name='rate',
            field=models.FloatField(blank=True, verbose_name='正解率'),
        ),
        migrations.AlterField(
            model_name='evaluation201606',
            name='time',
            field=models.FloatField(blank=True, verbose_name='時間'),
        ),
    ]
