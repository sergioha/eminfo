# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=10)),
                ('nombre_evento', models.TextField(max_length=200)),
                ('fecha_evento', models.DateField()),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
    ]
