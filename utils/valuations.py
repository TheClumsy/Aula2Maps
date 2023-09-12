from locations.models import Space
from valuations.models import Valuation
from django.contrib import messages


def show_valuations(request):
    result = request.POST.copy()

    name = result['nom']

    labels = ['Nom', 'Espai', 'Email', 'Telefon', 'Web']
    data = Space.objects.all().filter(nom=name).values_list('nom', 'espai', 'email', 'telefon', 'web')[0]
    all_valuations = Valuation.objects.all().filter(nom=name).values_list('titol', 'valoracio')

    useful_data = [value for value in [data[0], data[1], data[2], data[3], data[4]] if value]
    valuations = {space[0]: space[1] for space in all_valuations}

    if not valuations:
        messages.info(request, 'No hi ha valoracions disponibles')

    return valuations, name, useful_data, labels
