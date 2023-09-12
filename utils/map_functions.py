import folium
import branca
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Define the path to the templates directory
templates_dir = Path(__file__).resolve().parent.parent / 'locations' / 'templates'

# Create a Jinja2 environment with a loader
jinja2_env = Environment(loader=FileSystemLoader(str(templates_dir)))

def generate_popup(space_name):
    template = jinja2_env.get_template('popup.html')
    rendered_template = template.render(information=space_name)
    return rendered_template


def generate_color_by_space(space: str):
    color_mapping = {'Escola': 'red', 'Casa de Colònies': 'blue', 'Parc': 'green', 'Activitat': 'yellow'}

    return color_mapping[space]


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

    popup_html = generate_popup(name)
    iframe = branca.element.IFrame(html=popup_html, width=200, height=100)
    popup = folium.Popup(iframe, max_width=500)

    folium.Marker(location=coordinates, tooltip=name, icon=folium.Icon(color=color), popup=popup).add_to(catalonia_map)

    return catalonia_map
