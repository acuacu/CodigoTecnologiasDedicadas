# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculums', '0009_auto_20180412_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContadorDeCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contadorCurriculum', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='curriculum',
            name='FechaDeCreacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]