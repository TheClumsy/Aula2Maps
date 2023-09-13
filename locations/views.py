from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.urls import reverse
from utils.map_functions import generate_map
from utils.locations import check_location, search_for_space
from utils.coordinates import coordinates_format
from utils.map_functions import create_marker
from .models import Space


def map_page(request):
    """
    It brings us to the map page
    :param request: django request
    :return: it brings us to the map page
    """

    if request.method == 'POST':
        result = request.POST.copy()

        catalonia_map = result['catalonia_map']
        nom_escola = result['nom_escola']
        radius = result['radius']

        return render(request, 'map.html', {'catalonia_map': catalonia_map, 'nom_escola': nom_escola, 'radius': radius})

    catalonia_map = generate_map()
    return render(request, 'map.html', {'catalonia_map': catalonia_map._repr_html_()})


def search_page(request):
    catalonia_map = generate_map()
    popup_url = reverse('popup')

    if request.method == 'POST':
        result = request.POST.copy()
        catalonia_map = result.get('catalonia_map', generate_map())

        try:
            result, catalonia_map = search_for_space(request, catalonia_map)

        except IndexError:
            messages.error(request, "Escola no trobada a la base de dades!")
            catalonia_map = generate_map()
            return render(request, 'search.html', {'catalonia_map': catalonia_map._repr_html_()})

        except AssertionError:
            catalonia_map = generate_map()
            return render(request, 'search.html', {'catalonia_map': catalonia_map._repr_html_()})

        try:
            result['catalonia_map'] = catalonia_map._repr_html_()

        except AttributeError:
            result['catalonia_map'] = catalonia_map

        result['popup'] = popup_url

        return render(request, 'search.html', result)

    return render(request, 'search.html', {'catalonia_map': catalonia_map._repr_html_()})


@staff_member_required
def show_full_map(request):
    catalonia_map = generate_map()

    if request.method == 'POST':
        result = request.POST.copy()

        schools = result.get('nom_escola', None)
        house = result.get('casa_colonies', None)
        parks = result.get('parc', None)
        activities = result.get('activitat', None)

        options = [schools, house, parks, activities]

        selected_options = [option for option in options if option]

        spaces = Space.objects.all().filter(espai__in=selected_options).values_list('nom', 'coordenades', 'espai')

        for space in spaces:
            name = space[0]
            coordinates = coordinates_format(space[1])
            type_space = space[2]

            catalonia_map = create_marker(catalonia_map, coordinates, type_space, name)

    return render(request, 'full_map.html', {'catalonia_map': catalonia_map._repr_html_()})


@staff_member_required
def add_location(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login_page'))

    catalonia_map = generate_map()

    if request.method == "POST":
        result, catalonia_map = check_location(request, catalonia_map)
        result['catalonia_map'] = catalonia_map._repr_html_()
    else:
        result = {'catalonia_map': catalonia_map._repr_html_()}

    return render(request, 'add_locations.html', result)
