# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 17:28
from __future__ import unicode_literals

import Curriculums.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculums', '0016_auto_20180509_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diplomas',
            name='diploma',
            field=models.ImageField(blank=True, null=True, upload_to=Curriculums.models.generate_path_diploma),
        ),
    ]
