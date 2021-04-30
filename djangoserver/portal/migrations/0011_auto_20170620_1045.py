# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20170620_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portal.Personaldetails'),
        ),
        migrations.AlterField(
            model_name='responses',
            name='q1',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True),
        ),
        migrations.AlterField(
            model_name='responses',
            name='q2',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True),
        ),
        migrations.AlterField(
            model_name='responses',
            name='q3',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True),
        ),
        migrations.AlterField(
            model_name='responses',
            name='q4',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True),
        ),
        migrations.AlterField(
            model_name='responses',
            name='q5',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True),
        ),
    ]