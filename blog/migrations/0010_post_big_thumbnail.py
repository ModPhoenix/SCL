# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171109_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='big_thumbnail',
            field=models.BooleanField(default=False, help_text='Если отмечено, на превью будет большая миниатюра.', verbose_name='Большая миниатюра'),
        ),
    ]