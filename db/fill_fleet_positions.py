from db import Database

DATA_SOURCE_FILE = "data/positions_real_time.txt"

POSITIONS = [["37.7791648", "-122.42002"], ["37.7782595", "-122.4198174"],
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


INSERT_QUERY = """
INSERT INTO fleet_positions (car_id, logdate, position)
    VALUES ({car_id}, now(), ST_SetSRID(ST_MakePoint({lng}, {lat}), 4326));
"""


class FleetPositions(Database):

    def create_table(self):
        db.execute_file("sql/create_fleet_positions.sql")

    def fill_table(self):
        query = ""
        with open(DATA_SOURCE_FILE, 'r') as positions_file:
            for line in iter(positions_file):
                coordinates = line.split(" ")
                query += INSERT_QUERY.format(car_id=1,
                                             lat=coordinates[0],
                                             lng=coordinates[1])
        db.execute_query(query)

if __name__ == '__main__':
    db = FleetPositions()
    db.create_table()
    db.fill_table()
