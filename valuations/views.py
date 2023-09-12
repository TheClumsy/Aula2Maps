from django.shortcuts import render
from .forms import ValuationForm
from django.contrib import messages
from utils.valuations import show_valuations


def add_valuations(request):
    if request.method == 'POST':
        result = request.POST.copy()
        form = ValuationForm(result or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Valoració guardada correctament!')

        else:
            messages.error(request, 'ERROR: Valoració no guardada')

    return render(request, 'add_valuations.html', {})


def valuations_page(request):
    name = request.GET.get('name', None)

    if request.method == 'POST':
        try:
            result, name, data, labels = show_valuations(request)

            return render(request, 'valuations.html', {'display': True, 'valuations': result, 'name': name,
                                                       'information': data, 'labels': labels})
        except IndexError:
            pass

    return render(request, 'valuations.html', {'display': False, 'name': name})
