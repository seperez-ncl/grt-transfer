# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='tasa_cambio',
            field=models.FloatField(blank=True, default=0),
        ),
    ]