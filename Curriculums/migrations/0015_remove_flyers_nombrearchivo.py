# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculums', '0014_auto_20180509_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flyers',
            name='NombreArchivo',
        ),
    ]
