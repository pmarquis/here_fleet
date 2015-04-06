import os
import csv
from django.contrib.gis.geos import Point
from models import VehiclePositions, VehicleRoutes
from django.contrib.gis.geos import LineString


csv_vehicle_positions = 'data/vehicle_positions.csv'
file_vehicle_routes = 'data/vehicle_routes.txt'


def load_vehicle_positions():
    vehicle_positions_src = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     csv_vehicle_positions)
        )
    reader = csv.DictReader(open(vehicle_positions_src, 'rb'), delimiter=",")
    for line in reader:
        # car, lat, lng
        car = int(line.pop('car'))
        lat = float(line.pop('lat'))
        lng = float(line.pop('lng'))

        VehiclePositions(car=car,
                         position=Point(lng, lat)
                         ).save()


def load_vehicle_routes():
    """
    Load data car, polyline
    """
    vehicle_routes_src = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     file_vehicle_routes)
        )
    f = open(vehicle_routes_src, 'r')
    coordinates_list = []
    for coordinates in f.readlines():
        lat, lng = map(float, coordinates.split(','))
        coordinates_list.append((lat, lng))
    polyline = LineString(coordinates_list)

    VehicleRoutes(car=1, polyline=polyline).save()


# from fleet import load; load.run
def run():
    load_vehicle_positions()
    load_vehicle_routes()
