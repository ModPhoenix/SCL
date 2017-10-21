# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 11:27
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='sd', upload_to='sssssss'),
            preserve_default=False,
        ),
    ]
