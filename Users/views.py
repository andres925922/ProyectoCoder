import re
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
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


# -----------------------------------------------------
# MENSAJERÍA
# -----------------------------------------------------

# Vista para listar los hilos de un usuario
def get_room(request):
    if request.method == "GET":
        all_users = User.objects.exclude(username = request.user)
        rooms = User.objects.get(username=request.user).rooms.all()
        users = rooms[0].users.all()
        messages = rooms[0].messages.all()
        print(request.user, rooms[0], messages, users)
        return render(
            request=request, 
            template_name='Messenger/room_list.html', 
            context={
                'rooms': rooms,
                'all_users': all_users
                }
        )



class Room_List_View(TemplateView):
    template_name = 'Messenger/room_list.html'

# Vista para listar todos los mensajes de un hilo
class Room_Detail_View(DetailView):
    model = Room
    template_name: str = 'Messenger/room_detail.html'

    def get_object(self):
        obj = super(Room_Detail_View, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj


def start_room(request, username):
    user = get_object_or_404(User, username=username)
    hilo = Room.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[hilo.pk]))

def add_message(request, pk):
    content = request.GET.get('content', None)
    if content:
        hilo = get_object_or_404(Room, pk=pk)
        message = Message.objects.create(sender = request.user, body=content)
        hilo.messages.add(message)

    return JsonResponse({'creado': True})
