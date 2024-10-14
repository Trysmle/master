# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-25 16:27
from __future__ import unicode_literals

from django.db import migrations

def fill_session_unused_question_count(apps, schema_editor):
    Session = apps.get_model('exams', 'Session')

    for session in Session.objects.all():
        unused_question_count = session.questions.filter(is_deleted=False,
                                                         is_approved=True)\
                                                 .exclude(answer__session=session)\
                                                 .distinct()\
                                                 .count()
        session.unused_question_count = unused_question_count
        session.save()

def empty_session_unused_question_count(apps, schema_editor):
    Session = apps.get_model('exams', 'Session')
    Session.objects.update(unused_question_count=0)

class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0093_session_unused_question_count'),
    ]

    operations = [
        migrations.RunPython(fill_session_unused_question_count,
                             reverse_code=empty_session_unused_question_count)
    ]