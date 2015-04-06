# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehiclePositions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('car', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleRoutes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('car', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('polyline', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
    ]
