# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_app', '0005_auto_20170422_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price')),
                ('currency', models.CharField(max_length=5, verbose_name='currency')),
                ('url', models.CharField(max_length=200)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper_app.Product')),
            ],
        ),
    ]
