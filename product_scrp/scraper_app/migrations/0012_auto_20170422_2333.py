# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_app', '0011_auto_20170422_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='upddt',
            field=models.DateTimeField(default='2017-04-22 20:33:39', verbose_name='date updated'),
        ),
    ]
