# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 00:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170527_0759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '', 'verbose_name_plural': '人物'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '', 'verbose_name_plural': '用户'},
        ),
    ]
