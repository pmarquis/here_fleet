from db import Database

DATA_SOURCE_FILE = "data/positions_by_day.txt"

INSERT_QUERY = """
INSERT INTO fleet_positions_by_day (car_id, day, geometry)
    VALUES ({car_id}, now(), ST_GeomFromText('LINESTRING({polyline})', 4326));
"""


class FleetPositionsByDay(Database):

    def create_table(self):
        db.execute_file("sql/create_fleet_positions_by_day.sql")

    def fill_table(self):
        coordinates = []
        with open(DATA_SOURCE_FILE, 'r') as positions_file:
            coordinates = positions_file.readlines()
        polyline = ",".join(coordinates)
        polyline.strip('\n')
        query = INSERT_QUERY.format(car_id=1,
                                    polyline=polyline)
        db.execute_query(query)

if __name__ == '__main__':
    db = FleetPositionsByDay()
    db.create_table()
    db.fill_table()
