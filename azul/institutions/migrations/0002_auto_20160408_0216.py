# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliates',
            name='comment',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='affiliates',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='affiliates',
            name='phone',
            field=models.CharField(default=datetime.datetime(2016, 4, 8, 7, 16, 16, 293000, tzinfo=utc), max_length=55),
            preserve_default=False,
        ),
    ]
