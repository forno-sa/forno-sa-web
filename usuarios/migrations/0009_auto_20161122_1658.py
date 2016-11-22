# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20161122_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.CharField(verbose_name='Nome de usuário', max_length=50),
        ),
    ]
