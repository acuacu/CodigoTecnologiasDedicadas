# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 16:21
from __future__ import unicode_literals

import Curriculums.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculums', '0013_flyers_flyers'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyers',
            name='NombreArchivo',
            field=models.CharField(default='Agregar una Imagen', max_length=256),
        ),
        migrations.AlterField(
            model_name='flyers',
            name='flyers',
            field=models.ImageField(blank=True, null=True, upload_to=Curriculums.models.generate_path_flyer),
        ),
        migrations.AlterField(
            model_name='flyers',
            name='link',
            field=models.CharField(default='Agregar un link', max_length=256),
        ),
    ]
