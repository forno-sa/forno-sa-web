# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafico',
            name='tempo',
            field=models.TimeField(verbose_name='Tempo'),
        ),
    ]
