import unittest
from db import Database


class TestFleetPositions(unittest.TestCase):

    def test_select(self):
        query = """ select st_x(position), st_y(position)
 from fleet_positions """
        db = Database()
        rows = db.execute_query(query, select_query=True)
        lng, lat = rows[0]
        self.assertEqual(int(lat), 37)
        self.assertEqual(int(lng), -122)


unittest.main()
