# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20161122_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=10, verbose_name='Senha', default='password'),
            preserve_default=False,
        ),
    ]
