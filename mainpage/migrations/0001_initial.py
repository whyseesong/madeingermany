# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=20)),
                ('device_id', models.CharField(max_length=20)),
                ('is_attestated', models.BooleanField(default=False)),
                ('attestated_time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=10)),
                ('device_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Device')),
            ],
        ),
    ]
