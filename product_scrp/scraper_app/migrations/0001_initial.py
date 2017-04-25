# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('gtin', models.CharField(max_length=200, verbose_name='GTIN code')),
                ('code', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Product Price')),
                ('upddt', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
