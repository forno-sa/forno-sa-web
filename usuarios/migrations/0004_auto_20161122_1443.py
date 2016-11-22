# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20161122_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sobrenome',
            field=models.EmailField(verbose_name='Email', max_length=50),
        ),
    ]
