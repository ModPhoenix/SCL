# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата Создания'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата Редактирования'),
        ),
    ]