# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 07:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_auto_20170626_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='Story',
            new_name='story',
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='Storyid',
            new_name='storyid',
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='Time',
            new_name='time',
        ),
    ]
