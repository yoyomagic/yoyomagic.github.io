# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-18 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]