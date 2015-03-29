import unittest
from db import Database


class TestFleetPositions(unittest.TestCase):

    def get_polyline_from_linestring(self, db_linestring):
        linestring = db_linestring.replace("LINESTRING(", "").replace(")", "")
        coordinates = linestring.split(',')
        return [map(float, coordinate.split(" "))
                for coordinate in coordinates]

    def test_select(self):
        query = """ SELECT ST_AsText(geometry)
        FROM fleet_positions_by_day where car_id=1; """
        db = Database()
        rows = db.execute_query(query, select_query=True)
        polyline = self.get_polyline_from_linestring(rows[0][0])
        lat, lng = polyline[0]
        self.assertEqual(int(lat), 37)
        self.assertEqual(int(lng), -122)


unittest.main()
