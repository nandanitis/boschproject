# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-20 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissioncomputedscore',
            name='weights',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]