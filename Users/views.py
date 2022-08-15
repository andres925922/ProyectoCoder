import re
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from Artistas.views import render_view_artistas
from Users.forms.messenger_form import Message_Form, New_Room_Form
from .forms.user_form import User_Auth_Form, User_Creation_Form, User_Update_Form
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Avatar, Room, Message
from .services.user_service import get_my_user
from django.contrib.auth.models import User
from Base.services.base_service import get_avatar, get_information

from Clientes.views import render_view_clientes

from Base.exceptions import EntityCouldNotBeenCreated, BaseEntityNotFoundError

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
    else:

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

    username = request.user

    if request.user.is_authenticated:
        information = get_information(request.user)
    else:
        information = {}

    try:
        usuario = get_my_user(username=username)
    except:
        return redirect(request_login)

    if request.method == "POST":
        form = User_Update_Form(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect(render_view_artistas)
    else:
        form = User_Update_Form(instance = usuario)

    information['form'] = form
    information['usuario'] = usuario.username
    # information['avatar_form'] = get_avatar(usuario)


    return render(request, 'Users/user_update_form.html', context = information)

def logout_view(request):
    logout(request)
    return redirect(render_view_artistas)


# -----------------------------------------------------
# MENSAJERÍA
# -----------------------------------------------------

# Vista para listar los hilos de un usuario
@login_required
def get_room(request):

    """
    Función que nos permite listar todos los hilos de conversación abiertos entre usuarios para luego al dar click sobre alguno de ellos nos permita dirigirnos al hilo propiamente dicho.
    No toma parámetros.

    """
    information = get_information(request.user)

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

        information['rooms'] = lista_rooms
        information['all_users'] = all_users


        return render(
            request=request, 
            template_name='Messenger/room_list.html', 
            context=information
        )

@login_required
def get_conversation(request, pk = None, to = None):

    """ 
    Función que nos permite traer todos los mensajes pertenecientes a un hilo de conversación
    pk:int
    to:int
    Deben pasarse como parámetros la id de la room o hilo a la cual estamos haciendo referencia y además el destinatario que viene al cliclear sobre el hilo que queremos abrir de la página de mensajes

    """
    information = get_information(request.user)
    user = User.objects.get(id = request.user.id)
    room = Room.objects.get(id = pk)
    para = room.users.filter(id = to)[0]
    messages = room.messages.all()

    if room == None:
        start_room(user, para)
        

    if request.method == "POST":
        data = request.POST
        form = Message_Form(data=data)
        print(form)
        if form.is_valid():
            add_message(form, room.id)    

    form = Message_Form(initial={
            "sender" : user
    })

    information['msg'] = messages
    information['form'] = form

    return render(
        request=request,
        template_name='Messenger/room_detail.html',
        context=information
    )

def start_room(username1, username2):
    """
    Función que recibe como parámetros dos usuarios e inicia un nuevo hilo o room en caso de que no exista
    username1:str
    username2:str
    """
    user = get_object_or_404(User, username=username1)
    hilo = Room.objects.find_or_create(user, username2)
    return hilo

def add_message(message, room_id):
    """
    Función que nos permite agregar un mensaje al hilo.
    room_id:int
    Toma como parámetro la ide de la room o hilo de manera de poder vincular el mensaje al hilo.

    """

    try:
        hilo = Room.objects.get(id = room_id)
        message = Message.objects.create(
            sender = message.cleaned_data['sender'], 
            body = message.cleaned_data['body']
        )
        hilo.messages.add(message)
    except:
        raise EntityCouldNotBeenCreated('Ha ocurrido un error al crear el mensaje')

@login_required
def new_message(request):
    users = User.objects.exclude(username = request.user.username)

    if request.method == 'POST':
        data = request.POST
        print(data)

        try:
            sender = User.objects.get(id = request.user.id)
            to = User.objects.get(id = data['userid'])
        except:
            raise BaseEntityNotFoundError('Entidades no encontradas')

        room = Room.objects.find_or_create(
            user1 = sender,
            user2 = to
        )

        if room:
            return redirect(reverse('detailed', kwargs={
                'pk': room.id,
                'to' : data['userid']
            }))
            # return redirect(get_conversation, kwargs=
            # {'pk' : room.id,
            # 'to' : to.id} 
            # )

    return render(
        template_name = 'Messenger/nuevo_mensaje.html',
        request = request,
        context = {
            'all_users' : users
        }
    )

