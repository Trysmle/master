# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-14 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_optional_group_instituion'),
        ('exams', '0095_group_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='groups_allowed_to_take',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Group'),
        ),
        migrations.AddField(
            model_name='exam',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]