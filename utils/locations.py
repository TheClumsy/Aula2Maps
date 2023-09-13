from .format import check_coordinates_format
from .coordinates import get_coordinates
from .map_functions import create_marker
from .distances import linear_distance
from .coordinates import coordinates_format
from django.contrib import messages
from locations.forms import SpaceForm
from locations.models import Space


def search_for_space(request, catalonia_map):
    result = request.POST.copy()

    school_name = result.get('nom_escola', None)
    radius = result.get('radius', None)

    casa_colonies = result.get('casa_colonies', None)
    parc = result.get('parc', None)
    activitat = result.get('activitat', None)

    options = [casa_colonies, parc, activitat]
    selected_spaces = [option for option in options if option is not None]

    school = Space.objects.all().filter(nom=school_name).values_list('coordenades', 'espai', 'email', 'telefon', 'web')
    spaces = Space.objects.all().filter(espai__in=selected_spaces).values_list('nom', 'coordenades', 'espai',
                                                                               'email', 'telefon', 'web')
    assert school

    solutions = {school_name: school[0]}

    solutions = linear_distance(solutions, school_name, spaces, radius)

    for name in solutions:
        try:
            coordinates = coordinates_format(solutions[name][0])
            space = solutions[name][1]
            catalonia_map = create_marker(catalonia_map, coordinates, space, name)

        except TypeError:
            messages.error(request, "ERROR: les dades introduïdes no són correctes!")

        except AttributeError:
            pass

    solutions['nom_escola'] = school_name
    solutions['radius'] = radius

    return solutions, catalonia_map


def check_location(request, catalonia_map):
    result = request.POST.copy()

    nom = result.get('nom', None)
    espai = result.get('espai', None)
    email = result.get('email', None)
    telefon = result.get('telefon', None)
    web = result.get('web', None)

    if result['coordenades']:
        result['coordenades'] = check_coordinates_format(result['coordenades'])

        form = SpaceForm(result or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Espai Guardat Correctament!'))

            return {}, catalonia_map

        else:
            messages.error(request, ("ERROR: el format de les dades no és correcte"))

    else:
        result['coordenades'] = get_coordinates(nom)

        try:
            catalonia_map = create_marker(catalonia_map, result['coordenades'], espai, nom)
            messages.info(request, ('Comprova que les coordenades siguin correctes. Pren CERCAR per acceptar. Sobreescriu les coordenades en cas contrari'))

        except (TypeError, KeyError):
            messages.error(request, ("ERROR: el format de les dades no és correcte"))

    coordenades = result['coordenades']

    return {'nom': nom, 'espai': espai, 'email': email, 'telefon': telefon, 'web': web, 'coordenades': coordenades}, \
        catalonia_map
