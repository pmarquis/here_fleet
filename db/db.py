import psycopg2

DB_CONNECTION = "dbname='{db}' user='{u}' host='{h}' password='{pwd}'"


class Database:
    def _open_connexion(self):
        cnt = DB_CONNECTION.format(db="here_fleet_db",
                                   u="here",
                                   h="localhost",
                                   pwd="nokia")
        try:
            self.connection = psycopg2.connect(cnt)
        except:
            print("Unable to connect to the database")
        self.cursor = self.connection.cursor()

    def _close_connexion(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def execute_file(self, file):
        self.execute_query(open(file, "r").read())

    def execute_query(self, query, select_query=False):
        rows = []
        self._open_connexion()
        self.cursor.execute(query)
        if select_query:
            rows = self.cursor.fetchall()
        self._close_connexion()
        return rows
