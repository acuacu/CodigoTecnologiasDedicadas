# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 04:40
from __future__ import unicode_literals

import Curriculums.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculums', '0010_auto_20180413_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='FotoDePerfil',
            field=models.ImageField(blank=True, null=True, upload_to=Curriculums.models.generate_path),
        ),
        migrations.AlterField(
            model_name='datosusuario',
            name='FotoDePortada',
            field=models.ImageField(blank=True, null=True, upload_to=Curriculums.models.generate_path),
        ),
    ]