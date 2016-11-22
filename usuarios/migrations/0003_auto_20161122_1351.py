# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20161103_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 11, 22, 15, 51, 32, 953778, tzinfo=utc), verbose_name='password', max_length=128),
            preserve_default=False,
        ),
    ]
