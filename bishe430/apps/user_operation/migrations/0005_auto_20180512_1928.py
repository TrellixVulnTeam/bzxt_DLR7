# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0004_auto_20180509_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explomatch',
            name='exploEvi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploMatchEvi', to='evis.exploEvi', verbose_name='对应的物证'),
        ),
        migrations.AlterField(
            model_name='explomatch',
            name='exploSample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exploMatchSample', to='samples.exploSample', verbose_name='对应的样本'),
        ),
    ]
