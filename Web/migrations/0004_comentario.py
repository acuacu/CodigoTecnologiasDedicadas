# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_usuarios_comentarios', models.CharField(max_length=1000)),
                ('text_del_comentario', models.CharField(max_length=1000)),
                ('fecha_de_comentario', models.DateTimeField(auto_now_add=True)),
                ('link_imagen_izquierda', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
