from tornado.ioloop import IOLoop
from tornado.web import Application, url

from handlers import FleetRealTimeHandler, VehicleRouteHandler, HelperHandler


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
