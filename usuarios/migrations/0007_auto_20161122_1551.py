# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_usuario_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=50, verbose_name='Senha'),
        ),
    ]
