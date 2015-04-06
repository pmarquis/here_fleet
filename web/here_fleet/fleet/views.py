import json
from django.shortcuts import render, HttpResponse
from fleet.models import VehiclePositions, VehicleRoutes


def home(request):
    return render(request, "fleet/home.html")


def get_vehicle_positions(request):
    """returns json response with coordinates of vehicles
    http://127.0.0.1:8000/getVehiclPositions/
    """
    coordinates = []
    data = VehiclePositions.objects.values().distinct('car')
    vehicles = [d['car'] for d in data]
    for vehicle in vehicles:
        data = VehiclePositions.objects.filter(
            car=str(vehicle)).order_by('datetime')
        position = data.values()[0]['position']
        lon_lat = [coords for coords in position]
        coordinates.append(lon_lat)
    return HttpResponse(json.dumps(coordinates),
                        content_type='application/json')


def get_vehicle_routes(request, car_id, start_date, end_date):
    """returns json response with routes of vehicles
    http://127.0.0.1:8000/getVehicleRoutes/car_id/start_date/end_date
    """
    data = VehicleRoutes.objects.values().filter(car=str(car_id))
    coordinates_list = data[0]['polyline']
    polyline = [map(float, coordinates)
                for coordinates in coordinates_list]
    return HttpResponse(json.dumps(polyline),
                        content_type='application/json')
