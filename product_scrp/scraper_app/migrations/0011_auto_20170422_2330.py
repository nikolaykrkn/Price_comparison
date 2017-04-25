# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_app', '0010_auto_20170422_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='brand',
            field=models.CharField(blank=True, max_length=200, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='color',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Product Price'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='size',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='vendor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=200, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, default='GBP', max_length=5, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gtin',
            field=models.CharField(blank=True, max_length=200, verbose_name='GTIN code'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=-1.0, max_digits=12, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
