from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from Base.exceptions import BaseEntityNotFoundError
from Discos.models import Discos, Genero
from django.http import HttpResponse, Http404
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


def formulario_disco(request):
    if request.method == 'POST':
        form_discos=Discosformularios(request.POST)
        print(form_discos)
        if form_discos.is_valid:
            informacion=form_discos.cleaned_data
            formulario=Discos(nombre=informacion['nombre_de_album'], anio=informacion['year_lanzamiento'])
            formulario.save()
            return render(request, 'Discos\template_discos\template_discos.html')
    else: 
        form_discos=Discosformularios()
    return render(request,'Discos/template_discos/template_discos.html'), {'form_discos':form_discos}
   


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
    template='Discos/template_discos/template_discos_detalle.html'


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
