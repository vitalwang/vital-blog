# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 01:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 1, 1, 28, 3, 622000, tzinfo=utc), verbose_name='\u53d1\u8868\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
