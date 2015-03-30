from tornado.web import RequestHandler

BASE_URL = "http://127.0.0.1:8888/"

FUNCTION = """
<br/>
<h2>{title}</h2>
<p><a href='{link}' style='color: #6495ED'>{link}</a></p>
"""


class HelperHandler(RequestHandler):

    def add_function(self, title, function):
        return FUNCTION.format(title=title, link=BASE_URL + function)

    def create_doc(self):
        doc = "<div style='color: #6495ED'>"
        doc += self.add_function("Helper", "")
        doc += self.add_function("Get real time fleet positions",
                                 "getRealTimePositions")
        doc += self.add_function("Get Vehicle Routes between two days",
                                 "getVehicleRoutes/car_id/start_date/end_date")
        doc += "</div>"
        return doc

    def get(self):
        self.write(self.create_doc())
