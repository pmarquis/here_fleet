import requests


BASE_URL = "http://127.0.0.1:8888/"


class TestFleetRealTimeHandler():

    def testValues(self):
        params = dict()
        params['car_id'] = 1
        params['start_date'] = "2015-01-01"
        params['end_date'] = "2015-31-12"
        url = BASE_URL + "getRealTimePositions"
        response = requests.get(url)
        polyline = response.json()
        assert(len(polyline) > 0)
        for coordinates in polyline:
            assert(coordinates[0] < 180.)
            assert(coordinates[0] > -180.)
            assert(coordinates[1] < 90.)
            assert(coordinates[1] < -90.)

if __name__ == '__main__':
    t = TestFleetRealTimeHandler()
    t.testValues()
