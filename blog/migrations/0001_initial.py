# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 11:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата изменения')),
                ('published', models.BooleanField(default=True, help_text='Решает будет ли запись видна на сайте.', verbose_name='Опубликовано')),
                ('moderation', models.BooleanField(default=False, help_text='Запись заблокирована модератором.', verbose_name='Модерация')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
