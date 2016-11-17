# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tratamento', '0003_auto_20161116_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo', models.TimeField(verbose_name='Temperatura')),
            ],
            options={
                'verbose_name_plural': 'Tempos',
                'verbose_name': 'Tempo',
            },
        ),
        migrations.RemoveField(
            model_name='grafico',
            name='temperatura',
        ),
        migrations.RemoveField(
            model_name='grafico',
            name='tratamento',
        ),
        migrations.RemoveField(
            model_name='tratamento',
            name='temperatura',
        ),
        migrations.RemoveField(
            model_name='tratamento',
            name='tempo',
        ),
        migrations.AddField(
            model_name='tratamento',
            name='temperatura_tratamento',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tratamento.Temperatura', verbose_name='Temperatura Máxima'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamento',
            name='temperaturas',
            field=models.ManyToManyField(related_name='temperatura_set', to='tratamento.Temperatura'),
        ),
        migrations.DeleteModel(
            name='Grafico',
        ),
        migrations.AddField(
            model_name='tratamento',
            name='tempo_tratamento',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tratamento.Tempo', verbose_name='Tempo de Tratamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamento',
            name='tempos',
            field=models.ManyToManyField(related_name='tempo_set', to='tratamento.Tempo'),
        ),
    ]
