# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SampleCount',
            new_name='CounterModel',
        ),
        migrations.RenameField(
            model_name='countermodel',
            old_name='num',
            new_name='count',
        ),
    ]
