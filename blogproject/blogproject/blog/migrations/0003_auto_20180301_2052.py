# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-01 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_meta_updatetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meta',
            old_name='user',
            new_name='provider',
        ),
    ]