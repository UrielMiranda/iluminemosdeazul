# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
    ]
