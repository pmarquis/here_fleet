import math


DELTA = 0.1


class SimplifyPolyline:

    def simplify_polyline(self, polyline):
        polyline_in_meter = self._get_polyline_in_meter(polyline)
        index_to_display = self._simplify_polyline(polyline_in_meter)
        return [point for point in polyline
                if polyline.index(point) in index_to_display]

    def _simplify_polyline(self, polyline):
        if len(polyline) < 2:
            return []
        first = polyline[0]
        last = polyline[-1]
        if len(polyline) == 2:
            return [first, last]
        max_distance = 0.
        farthest_index = 0
        for i in range(1, len(polyline)-1):
            dist = self._perpendicular_distance(polyline[i], first, last)
            if dist > max_distance:
                farthest_index = i
                max_distance = dist

        if max_distance > DELTA:
            return [first, last]

        index_to_display1 = self._simplify_polyline(
                polyline[0: farthest_index])
        index_to_display2 = self._simplify_polyline(
                polyline[farthest_index: -1])
        return index_to_display1 + [index + farthest_index
                                    for index in index_to_display2] \
            + [0, len(polyline)-1]

    def _perpendicular_distance(self, point, line_start, line_end):
        """
        Calculate the perpendicular distance from a point to a line.
        """
        x1, y1 = line_start
        x2, y2 = line_end
        vx, vy = point
        if x1 == x2:
            return abs(x1 - vx)
        m = (y2 - y1)/(x2 - x1)
        b = y1 - m*x1
        return abs(m * vx - vy + b)/math.sqrt(m*m + 1)

    def _haversine_distance(self, origin, destination):
        """
        Compute the distance in km between coordinates (lat, lng)
        """
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371  # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) \
            + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) \
            * math.sin(dlon/2) \
            * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d

    def _get_polyline_in_meter(self, polyline):
        new_polyline = []
        for point in polyline:
            lat_m = self._haversine_distance([point[0], 0], [0, 0])
            lng_m = self._haversine_distance([0, point[1]], [0, 0])
            new_polyline.append([lat_m, lng_m])
        return new_polyline


if __name__ == '__main__':
    sp = SimplifyPolyline()
    polyline = [[37.7892890286851, -122.412359611053],
                [37.7897977472977, -122.411587134857],
                [37.7899334050029, -122.410385505218],
                [37.7899334050029, -122.409098044891],
                [37.7901368910937, -122.408153907318]]
    print sp.simplify_polyline(polyline)
