from tornado.ioloop import IOLoop
from tornado.web import Application, url

from fleet_real_time_handler import FleetRealTimeHandler
from vehicle_routes_handler import VehicleRouteHandler
from helper_handler import HelperHandler


def make_app():
    return Application([
        url(r"/", HelperHandler),
        url(r"/getRealTimePositions", FleetRealTimeHandler),
        url(r"/getVehicleRoutes/(.*)", VehicleRouteHandler),
        ])


def main():
    app = make_app()
    app.listen(8888, address='127.0.0.1')
    IOLoop.current().start()


if __name__ == '__main__':
    main()
