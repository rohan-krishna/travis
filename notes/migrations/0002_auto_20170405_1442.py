# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 09:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 5, 9, 12, 23, 858000, tzinfo=utc)),
        ),
    ]
