# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_auto_20160408_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliates',
            name='category',
            field=models.CharField(default=datetime.datetime(2016, 4, 8, 7, 31, 40, 626000, tzinfo=utc), max_length=1, choices=[(b'1', b'Fundaciones'), (b'2', b'Colaboradores'), (b'3', b'Vocales')]),
            preserve_default=False,
        ),
    ]
