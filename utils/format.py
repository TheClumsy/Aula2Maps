
def check_coordinates_format(coordinates):
    if coordinates[0] != '(':
        return '(' + coordinates + ')'
    else:
        return coordinates
