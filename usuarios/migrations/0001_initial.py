# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254)),
                ('data_criacao', models.DateField(default=django.utils.timezone.now, verbose_name='Data de cadastro')),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matrícula')),
                ('senha', models.CharField(max_length=100, verbose_name='Senha')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nome de usuário')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
        ),
    ]
