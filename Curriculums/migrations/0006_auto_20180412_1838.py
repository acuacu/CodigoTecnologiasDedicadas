# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-12 21:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculums', '0005_datosusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='CuentaDelUsuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
