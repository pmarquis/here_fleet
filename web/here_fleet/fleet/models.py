from django.utils import timezone
from django.contrib.gis.db import models


class VehiclePositions(models.Model):
    """
    Vehicle positions data: id, car, date, (lat, lng)
    """
    id = models.AutoField(primary_key=True)
    car = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)
    position = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        # __str__ on Python 3
        return str(self.car)


class VehicleRoutes(models.Model):
    """
    Vehicle routes data: id, car, date, polyline
    """
    id = models.AutoField(primary_key=True)
    car = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)
    polyline = models.LineStringField()
    objects = models.GeoManager()

    def __unicode__(self):
        # __str__ on Python 3
        return str(self.car)
