# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rol', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApellidoPaterno', models.CharField(max_length=30)),
                ('ApellidoMaterno', models.CharField(max_length=30)),
                ('Nombres', models.CharField(max_length=30)),
                ('Titulo', models.CharField(choices=[('Est.', 'Estudiante'), ('Sr.', 'Señor'), ('Sra.', 'Señora'), ('Ing.', 'Ingeniero(a)'), ('Lic.', 'Licenciado(a)'), ('Arq.', 'Arquitecto(a)'), ('Dr.', 'Doctor'), ('Dra.', 'Doctora'), ('Mtr.', 'Master')], default='Est.', max_length=5)),
                ('CI', models.CharField(max_length=10, unique=True)),
                ('Correo', models.EmailField(max_length=50, unique=True)),
                ('Telefono', models.CharField(max_length=20)),
                ('Login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Login')),
                ('Rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Roles')),
            ],
        ),
    ]
