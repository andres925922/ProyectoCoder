from pdb import post_mortem
from django.shortcuts import render, HttpResponse, redirect

from Base.exceptions import BaseEntityNotFoundError
from Base.services.base_service import get_information
from .services.service_artistas import (
get_all_artistas, 
get_artista_por_nombre_y_apellido
)
from .services.service_bandas import (
    get_all_bandas,
    get_banda
)
from .forms.forms import Artista_Formulario, Banda_Formulario
from .models import Artista, Banda

# Create your views here.

def render_view_artistas(request):

    information = get_information(request.user)
    information['artistas'] = get_all_artistas()
  
    return render(
        request = request,
        template_name ='Artistas/template_artistas.html',
        context = information
    )

def render_view_bandas(request):

    information = get_information(request.user)
    information['bandas'] = get_all_bandas()

    return render(
        request = request,
        template_name='Bandas/template_bandas.html',
        context= information
    )

def render_view_formulario_bandas(request):
    if request.method == "POST":
        formulario = Banda_Formulario(request.POST)
        if formulario.is_valid:
            info = formulario.cleaned_data
            print(info)
            banda = Banda(
                nombre = info['nombre']
            )
            banda.save()
            return redirect(render_view_bandas)
    else:
        formulario = Banda_Formulario()

    return render(request, 'Artistas/formulario_banda.html', {'form' : formulario})

def render_view_formulario_artistas(request):

    if request.method == 'POST':
        formulario = Artista_Formulario(request.POST)
        if formulario.is_valid:
            try:
                banda = get_banda(request.POST['banda'])
                artista = Artista(
                    nombre = request.POST['nombre'],
                    apellido = request.POST['apellido'],
                    nombre_artistico = request.POST['nombre_artistico'],
                    banda = banda,
                    historia = request.POST['historia']
                )
                artista.save()
                return redirect(render_view_artistas)
            except BaseEntityNotFoundError as e:
                return HttpResponse('Ocurrió un error al buscar la banda')

    else:
        formulario = Artista_Formulario()

    return render(request, 'Artistas/formulario_artista.html', {'form' : formulario})

def render_artista_por_nombre_y_apellido(request):
    pass