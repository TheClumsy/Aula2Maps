from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def log_out(request):
    logout(request)
    messages.success(request, ('Sessió tancada correctament'))
    return render(request, 'login_page.html', {})


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(request, ('Usuari INCORRECTE! Torna-ho a intentar'))
            return redirect('/login/')

    return render(request, 'login_page.html', {})


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html', {})
