from db import Database


if __name__ == '__main__':
    db = Database()
    db.execute_query("sql/create_fleet_positions.sql")
