# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-02-13 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200213_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]