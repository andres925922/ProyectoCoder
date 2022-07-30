import re
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from Artistas.views import render_view_artistas
from Users.forms.messenger_form import Message_Form
from .forms.user_form import User_Auth_Form, User_Creation_Form, User_Update_Form
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, Http404, JsonResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .models import Avatar, Room, Message
from django.contrib.auth.models import User

from Clientes.views import render_view_clientes

from Base.exceptions import EntityCouldNotBeenCreated

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
                return redirect(render_view_artistas)
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


# -----------------------------------------------------
# MENSAJERÍA
# -----------------------------------------------------

# Vista para listar los hilos de un usuario
def get_room(request):
    if request.method == "GET":
        all_users = User.objects.exclude(username = request.user)
        rooms = User.objects.get(username=request.user).rooms.all()
        lista_rooms = []

        for room in rooms:
            for user in Room.objects.get(id = room.id).users.all():
                if user != request.user:
                    lista_rooms.append(
                        {'user': user, 'room': room}
                    )


        return render(
            request=request, 
            template_name='Messenger/room_list.html', 
            context={
                'rooms': lista_rooms,
                'all_users': all_users
                }
        )

    if request.methos == 'POST':
        print('hola')
    
def get_conversation(request, pk = None, to = None):

    user = User.objects.get(id = request.user.id)
    room = Room.objects.get(id = pk)
    para = room.users.filter(id = to)[0]
    messages = room.messages.all()

    if room == None:
        start_room(user, para)
        

    if request.method == "POST":
        data = request.POST
        form = Message_Form(data=data)
        if form.is_valid():
            print('Es válido')
            add_message(form, room.id)    

    form = Message_Form(initial={
            "sender" : user
    })

    return render(
        request=request,
        template_name='Messenger/room_detail.html',
        context={
            "msg": messages,
            "form": form
        }
    )

def start_room(username1, username2):
    user = get_object_or_404(User, username=username1)
    hilo = Room.objects.find_or_create(user, username2)
    return hilo

def add_message(message, room_id):
    # print(message.cleaned_data['sender'].id, message.cleaned_data['body'])
    # return
    try:
        hilo = Room.objects.get(id = room_id)
        message = Message.objects.create(
            sender = message.cleaned_data['sender'], 
            body = message.cleaned_data['body']
        )
        hilo.messages.add(message)
    except:
        raise EntityCouldNotBeenCreated('Ha ocurrido un error al crear el mensaje')

