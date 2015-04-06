# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0004_auto_20150404_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicleroutes',
            name='date',
        ),
        migrations.AddField(
            model_name='vehicleroutes',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
