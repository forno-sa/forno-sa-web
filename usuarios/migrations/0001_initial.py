# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254)),
                ('data_criacao', models.DateField(verbose_name='Data de cadastro', default=django.utils.timezone.now)),
                ('matricula', models.CharField(unique=True, max_length=10, verbose_name='Matrícula')),
                ('senha', models.CharField(max_length=100, verbose_name='Senha')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Nome de usuário')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
        ),
    ]
