# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-19 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0079_add_edited_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duplicate',
            options={'ordering': ('question',)},
        ),
        migrations.AlterUniqueTogether(
            name='duplicate',
            unique_together=set([('container', 'question')]),
        ),
    ]