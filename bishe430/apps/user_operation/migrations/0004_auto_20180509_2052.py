# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20180508_2155'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='exlpoMatch',
            new_name='exploMatch',
        ),
    ]