from tornado.web import RequestHandler
import json

from db import Database
from simplify_polyline import SimplifyPolyline


POINTS = [["37.7791648", "-122.42002"], ["37.7782595", "-122.4198174"],
          ["37.7784848", "-122.4182189"], ["37.7786565", "-122.4165881"],
          ["37.7788067", "-122.4153006"], ["37.7787482", "-122.4152379"],
          ["37.7787638", "-122.4152148"], ["37.7796113", "-122.4138522"],
          ["37.7803838", "-122.4130583"], ["37.7810812", "-122.4122"],
          ["37.7819395", "-122.4110091"], ["37.7825618", "-122.4100971"],
          ["37.7827549", "-122.409786"], ["37.7833879", "-122.4088848"],
          ["37.7838278", "-122.4082947"], ["37.7848256", "-122.4070072"],
          ["37.7851045", "-122.4066854"], ["37.7858877", "-122.405709"],
          ["37.7867031", "-122.4047434"], ["37.7880335", "-122.4031234"],
          ["37.7890849", "-122.4018145"], ["37.7912951", "-122.398982"]]


class VehicleRouteHandler(RequestHandler):

    def get(self, args):
        car_id, start_date, end_date = args.split("/")
        polyline = self.get_last_positions_vehicle()
        self.write(json.dumps(polyline))
        # sp = SimplifyPolyline()
        # new_polyline = sp.simplify_polyline(polyline)
        # print("Remove {}% of points".format(
        #     (len(polyline) - len(new_polyline)) * 100 / len(polyline)))
        # self.write(json.dumps(new_polyline))

    def set_default_headers(self):
        self.set_header('Content-Type', 'text/plain')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods',
                        'GET, PUT, POST, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Content-Range, Content-Disposition, Content-Description')

    def get_last_positions_vehicle(self):
        # query = """ SELECT ST_AsText(geometry)
        query = """ SELECT ST_AsText(ST_Simplify(geometry, 0.0005))
        FROM fleet_positions_by_day where car_id=1; """
        db = Database()
        rows = db.execute_query(query, select_query=True)
        return self.get_polyline_from_linestring(rows[0][0])

    def get_polyline_from_linestring(self, db_linestring):
        linestring = db_linestring.replace("LINESTRING(", "").replace(")", "")
        coordinates = linestring.split(',')
        return [map(float, coordinate.split(" "))
                for coordinate in coordinates]
