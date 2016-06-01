# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='evaluation201606',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='お名前を入力してください', max_length=64, verbose_name='名前')),
                ('rate', models.FloatField(verbose_name='正解率')),
                ('time', models.FloatField(verbose_name='時間')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
        ),
    ]
