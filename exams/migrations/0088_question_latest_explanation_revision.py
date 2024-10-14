# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-23 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0087_rename_to_was_announced'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='latest_explanation_revision',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latst_of', to='exams.ExplanationRevision'),
        ),
    ]