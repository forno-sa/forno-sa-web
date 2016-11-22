# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20161122_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(verbose_name='Senha', max_length=100),
        ),
    ]
