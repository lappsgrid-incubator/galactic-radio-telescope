# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-18 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180618_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='file_size',
            field=models.BigIntegerField(null=True),
        ),
    ]
