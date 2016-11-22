# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('usuarios', '0009_auto_20161122_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set', to='auth.Group', verbose_name='groups', blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', to='auth.Permission', verbose_name='user permissions', blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.CharField(max_length=10, verbose_name='Matrícula', unique=True),
        ),
    ]
