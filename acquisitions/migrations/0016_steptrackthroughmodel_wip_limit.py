# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acquisitions', '0015_auto_20160630_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='steptrackthroughmodel',
            name='wip_limit',
            field=models.IntegerField(default=0),
        ),
    ]