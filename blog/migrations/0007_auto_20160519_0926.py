# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
