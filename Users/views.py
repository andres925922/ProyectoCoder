import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from Clientes.views import render_view_clientes

# Create your views here.

def request_login(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid:
            usr = request.POST['username']
            pwd = request.POST['password']

            user = authenticate(username=usr, password=pwd)
            if user is not None:
                login(request, user=user)
                return redirect(render_view_clientes)
            else:
                return HttpResponse("Error al loguear")

        else:
            return HttpResponse("Error en el formulario")

    form = AuthenticationForm()
    return render(request, 'Users/login.html', {"form": form} )
