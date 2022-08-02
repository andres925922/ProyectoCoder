from pdb import post_mortem
from django.shortcuts import render, HttpResponse, redirect

from Base.exceptions import BaseEntityNotFoundError
from Base.services.base_service import get_information
from .services.service_artistas import (
get_all_artistas,
get_artista, 
get_artista_por_nombre_y_apellido,
get_discos_y_bandas_por_artista
)
from .services.service_bandas import (
    get_all_bandas,
    get_banda
)
from .forms.forms import Artista_Formulario, Banda_Formulario
from .models import Artista, Banda

from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login/')
def render_view_artistas(request):

    if request.user.is_authenticated:
        information = get_information(request.user)
    else:
        information = {}

    information['artistas'] = get_all_artistas()
  
    return render(
        request = request,
        template_name ='Artistas/template_artistas.html',
        context = information
    )

@login_required(login_url='login/')
def render_view_artista_detalle(request, id):

    information = get_information(request.user)
    try:
        information['artista'] = get_artista(id = id)
        information['banda'] = information['artista'].banda
        information['discos'] = get_discos_y_bandas_por_artista(information['artista'].id)
    except:
        return redirect(render_view_artistas)
  
    return render(
        request = request,
        template_name ='Artistas/detalle_artista.html',
        context = information
    )

@login_required(login_url='login/')
def render_view_bandas(request):

    information = get_information(request.user)
    information['bandas'] = get_all_bandas()

    return render(
        request = request,
        template_name='Bandas/template_bandas.html',
        context= information
    )

@login_required(login_url='login/')
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

@login_required(login_url='login/')
def render_view_formulario_artistas(request):
    information = get_information(request.user)
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
                return HttpResponse('Ocurrió un error al guardar al artista')

    else:
        formulario = Artista_Formulario()
    information['form'] = formulario

    return render(request, 'Artistas/formulario_artista.html', information)

@login_required(login_url='login/')
def render_view_editar_artista(request, id):
    artista = get_artista(id=id)
    information = get_information(request.user)
    if request.method == 'POST':
        formulario = Artista_Formulario(request.POST, instance=artista)
        if formulario.is_valid:
            try:
                banda = get_banda(request.POST['banda'])
                # artista.nombre = request.POST['nombre'],
                # artista.apellido = request.POST['apellido'],
                # artista.nombre_artistico = request.POST['nombre_artistico'],
                # artista.banda = banda,
                # artista.historia = request.POST['historia']

                formulario.save()
                return redirect(render_view_artistas)
            except BaseEntityNotFoundError as e:
                return HttpResponse('Ocurrió un error al guardar el usuario')
    else:
        formulario = Artista_Formulario(
            instance=artista
        )
    information['form'] = formulario

    return render(request, 'Artistas/formulario_artista_edita.html', information)



@login_required(login_url='login/')
def render_artista_por_nombre_y_apellido(request):
    pass