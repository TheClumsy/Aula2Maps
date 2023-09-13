import folium


def generate_popup(name):
    link = f"""<a href="/valuations/?name={name}" target="_blank">Informació</a>"""
    popup = folium.Popup(link, max_width=500)
    return popup


def generate_color_by_space(space: str):
    color_mapping = {'Escola': 'red', 'Casa de Colònies': 'blue', 'Parc': 'green', 'Activitat': 'orange'}

    return color_mapping[space]


def generate_icon_by_space(space):
    icon_mapping = {'Escola': 'school', 'Casa de Colònies': 'shop', 'Parc': 'tree', 'Activitat': 'fly'}

    return icon_mapping[space]


def generate_map():
    """
    Function that generates Catalonia's map
    :return: the map of Catalonia
    """
    catalonia_coordinates = (41.8781, 1.7831)
    catalonia_map = folium.Map(location=catalonia_coordinates, zoom_start=8)

    return catalonia_map


def create_marker(catalonia_map, coordinates, space, name):
    color = generate_color_by_space(space)

    popup = generate_popup(name)

    folium.Marker(location=coordinates, tooltip=name, icon=folium.Icon(color=color), popup=popup).add_to(catalonia_map)

    return catalonia_map
