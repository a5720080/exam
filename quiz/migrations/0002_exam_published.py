# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]