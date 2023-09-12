import geocoder


def get_coordinates(name: str):
    location = geocoder.osm(name)

    if (location.lat, location.lng) == (None, None):
        return 0

    return location.lat, location.lng


def coordinates_format(string):
    string = str(string)
    string_list = string.strip('()').split(', ')
    return float(string_list[0]), float(string_list[1])
