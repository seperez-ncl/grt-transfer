# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20171028_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='nfactura',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]