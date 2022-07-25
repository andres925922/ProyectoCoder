import re
from django.shortcuts import render, redirect
from .forms.user_form import User_Auth_Form, User_Creation_Form, User_Update_Form
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from .models import Avatar

from Clientes.views import render_view_clientes

# Create your views here.

def request_login(request):

    if request.method == "POST":
        form = User_Auth_Form(request=request, data=request.POST)
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

    form = User_Auth_Form()
    return render(request, 'Users/login.html', {"form": form} )

def create_user(request):

    if request.method == "POST":
        form = User_Creation_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(render_view_clientes)
    else:
        form = User_Creation_Form()

    return render(request, 'Users/user_creation_form.html', {
        'form': form
    })


def edit_user(request):

    usuario = request.user

    if request.method == "POST":
        form = User_Update_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(render_view_clientes)
    else:
        form = User_Update_Form(initial={
            'email': usuario.email
        })

    return render(request, 'Users/user_update_form.html', {
        'form': form,
        'usuario': usuario
    })

def logout_view(request):
    logout(request)
    return redirect(render_view_clientes)
        
