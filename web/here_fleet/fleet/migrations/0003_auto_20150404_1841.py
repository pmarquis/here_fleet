# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_auto_20150404_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclepositions',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 4, 18, 41, 41, 693791)),
        ),
    ]
