from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from Base.exceptions import BaseEntityNotFoundError
from Discos.models import Discos, Genero
from django.http import HttpResponse, Http404

from ProyectoCoder.settings import BASE_DIR
from .discos_forms import Discosformularios
from django.views.generic import ListView, UpdateView
from django.views.generic import DetailView, CreateView
from django.views.generic import ListView
from django.views.generic import DetailView

from Base.services.base_service import get_information

from Discos.forms.discos_form import(
    Generos_Form,
    Discos_Form,
    Canciones_Form
)

from Discos.services.discos_service import Genero_Service
genero_service = Genero_Service()

# Create your views here.

def render_view_discos(request):
    discos=Discos.objects.all()
    if len(discos) == 0: 
        return HttpResponse('El artista seleccionado no tiene discos')
    else:
        return HttpResponse(discos[0].nombre)

def busqueda_discos(request):
    return render(request, 'Discos/template_discos/busqueda_discos.html')

def buscar(request):
    respuesta=f'Estoy buscando el disco nombre: {request.GET[Discos.nombre]}'
    return HttpResponse(respuesta)

class Discoslist(ListView):
    model=Discos
    template_name = 'discos_list.html'

class Discosdetalle(DetailView):
    model=Discos
    template_name='discos_detail.html'


def formulario_disco(request):
    """
    # Función para crear discos
    """
    if request.method == 'POST':
        form_discos=Discosformularios(request.POST)
        if form_discos.is_valid:
            form_discos.save()
            return redirect('discos-list')
    else: 
        form_discos=Discosformularios()

    return render(request,'template_discos.html', {'form_discos':form_discos})

def eliminar_disco(request, id_disco = None):
    """
    # Función para eliminar discos
    """
    if id_disco != None and request.method == "GET":
        
        disco = Discos.objects.filter(id = id_disco)[0]

        if disco:
            # disco.deleted == True
            disco.delete()

    return redirect('discos-list')



def editar_disco(request, id_disco = None):
    """
    # Función para actualizar discos
    """
    if id_disco == None:
        return redirect('discos-list')

    try:
        disco = Discos.objects.get(id = id_disco)
    except:
        return redirect('discos-list')

    if request.method == "POST":
        formulario = Discosformularios(request.POST, request.FILES, instance=disco)
        if formulario.is_valid:
            formulario.save()
            return redirect('discos-list')

    else:
        formulario = Discosformularios(instance=disco)

    return render(request, 'editardiscos.html', {'form' : formulario})




# ***********************************************************
# vistas de genero
# ***********************************************************


def get_all_generos(request):

    information = get_information(request.user)
    information['generos'] = genero_service.get_generos()

    return render(
        request = request,
        template_name='Generos/template_generos.html',
        context = information
    )

def create_genero(request):

    information = get_information(request.user)

    if request.method == 'POST':
        form_generos = Generos_Form(request.POST)
        if form_generos.is_valid():
            form_generos.save()
            return redirect(get_all_generos)
        else:
            raise Http404('Ha ocurrido un error')

    else:
        form_generos = Generos_Form()
        information['form'] = form_generos

    return render(
        request = request,
        template_name='Generos/create_form.html',
        context = information
    )

def update_genero(request, id = None):

    information = get_information(request.user)
    genero = Genero.objects.get(id=id)

    if request.method == 'POST':

        form_generos = Generos_Form(request.POST, instance=genero)
        if form_generos.is_valid():
            form_generos.save()
            return redirect(get_all_generos)
        # else:
        #     return Http404()

    else:
        form_generos = Generos_Form( instance=genero)
        information['form'] = form_generos

    return render(
        request = request,
        template_name='Generos/update_form.html',
        context = information
    )

def delete_genero(request, id = None):
    if id != None:
        try:
            genero_service.baja_genero(data=id)
        except BaseEntityNotFoundError:
            return Http404('Ocurrió un error')

    return redirect(get_all_generos)
