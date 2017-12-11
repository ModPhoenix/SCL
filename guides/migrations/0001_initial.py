# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 13:30
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
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Решает будет ли запись видна на сайте.', verbose_name='Опубликовано')),
                ('moderation', models.BooleanField(default=False, help_text='Если отмечено, запись заблокирована модератором.', verbose_name='Модерация')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.SlugField(help_text='Слаг — это вариант названия, подходящий для URL. Обычно содержит только латинские буквы в нижнем регистре, цифры и дефисы.', max_length=60, verbose_name='Слаг')),
                ('content', models.TextField(verbose_name='Контент')),
                ('excerpt', models.TextField(blank=True, help_text='По Умолчанию первый абзац Контента, при необходимости можно изменить.', verbose_name='Описание')),
                ('ordering', models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Сортировка')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Миниатюра')),
                ('big_thumbnail', models.BooleanField(default=False, help_text='Если отмечено, на превью будет большая миниатюра.', verbose_name='Большая миниатюра')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Гайд',
                'verbose_name_plural': 'Гайды',
                'ordering': ['-created_at'],
            },
        ),
    ]