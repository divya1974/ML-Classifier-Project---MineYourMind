# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_auto_20170621_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='Email_id',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]