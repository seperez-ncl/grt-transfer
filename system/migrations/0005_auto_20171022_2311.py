# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_remove_concepto_operacion_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concepto_operacion',
            name='concepto',
            field=models.CharField(default='a', max_length=50, verbose_name='concepto'),
        ),
        migrations.AlterField(
            model_name='concepto_operacion',
            name='observaciones',
            field=models.TextField(default='sdsd', verbose_name='observaciones'),
        ),
    ]
