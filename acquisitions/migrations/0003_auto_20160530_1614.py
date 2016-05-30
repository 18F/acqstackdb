# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acquisitions', '0002_auto_20160527_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquisition',
            name='amount_of_competition',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='award_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='competition_strategy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='contract_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='contracting_office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acquisitions.ContractingOffice'),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='contracting_officer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acquisitions.ContractingOfficer'),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='contracting_officer_representative',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acquisitions.COR'),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='dollars',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='naics',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='period_of_performance',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='procurement_method',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='product_owner',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='rfq_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='set_aside_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='subagency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acquisitions.Subagency'),
        ),
    ]
