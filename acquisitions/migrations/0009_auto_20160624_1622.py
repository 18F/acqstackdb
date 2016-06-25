# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 16:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('acquisitions', '0008_auto_20160623_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquisition',
            name='award_status',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='track', chained_model_field='track', on_delete=django.db.models.deletion.CASCADE, to='acquisitions.AwardStatus'),
        ),
    ]