# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0006_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
    ]
