# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operador',
            name='estatus',
        ),
        migrations.AddField(
            model_name='operador',
            name='estado',
            field=models.BooleanField(default=False, help_text='Seleccione estado (Libre-Ocupado)', verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='camion',
            name='estado',
            field=models.CharField(choices=[('0', 'Libre'), ('1', 'Ocupado'), ('2', 'Arrendado')], default=0, max_length=2, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='operador',
            name='ciudad',
            field=models.CharField(default='Nuevo Laredo', max_length=20, verbose_name='ciudad'),
        ),
    ]
