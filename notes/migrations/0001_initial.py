# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 09:09
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Note', max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Notebook', max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2017, 4, 5, 9, 9, 53, 235000, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2017, 4, 5, 9, 9, 53, 235000, tzinfo=utc))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='notebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Notebook'),
        ),
    ]