# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_auto_20150404_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclepositions',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
