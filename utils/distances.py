import math
from utils.coordinates import coordinates_format


def linear_distance(solutions, school_name, spaces, radius):

    if radius:
        radius = int(radius)
        earth_radius_km = 6371.0

        x1_coordinate, y1_coordinate = coordinates_format(solutions[school_name][0])

        for space in spaces:
            x2_coordinate, y2_coordinate = coordinates_format(space[1])
            delta_lat = math.radians(float(x2_coordinate)) - math.radians(float(x1_coordinate))
            delta_lon = math.radians(float(y2_coordinate)) - math.radians(float(y1_coordinate))

            a = math.sin(delta_lat / 2) ** 2 + math.cos(float(x1_coordinate)) * math.cos(float(x2_coordinate)) * math.sin(delta_lon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

            if earth_radius_km * c < radius:
                solutions[space[0]] = space[1:]

    return solutions
