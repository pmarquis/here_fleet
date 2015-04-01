from fabric.api import local, cd


def start():
    local("python webservice/server.py")


def functional_tests():
    local("nosetests webservice/tests/functional")


def fill_database():
    with cd("db/"):
        local("python fill_fleet_positions.py")
        local("python fill_fleet_positions_by_day.py")
