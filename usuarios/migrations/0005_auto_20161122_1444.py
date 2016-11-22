# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20161122_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=datetime.datetime(2016, 11, 22, 16, 44, 56, 600143, tzinfo=utc), max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(max_length=50, verbose_name='Sobrenome'),
        ),
    ]
