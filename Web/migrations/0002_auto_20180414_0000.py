# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Respondido',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='mostrar',
            field=models.BooleanField(default=False),
        ),
    ]
