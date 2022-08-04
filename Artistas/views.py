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
    create_or_update_banda,
    delete_banda,
    get_all_bandas,
    get_banda
)
from .forms.forms import Artista_Formulario, Banda_Formulario
from .models import Artista, Banda

from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login/')
def render_view_artistas(request):
    """
    # Esta vista permite listar todos los artistas.
    # Si el usuario está logueado podrá ver sus datos y su avatar y navegar a otras ventanas, de lo contrario no podrá hacer nada mas que logurarse
    """

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
    """
    # Vista que permite listar la data de un artista, sus discos y la banda a la que pertenece
    """

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

    """ 
    # Vista que permite listar las bandas cargadas en la base de datos
    # Tomamos el mismo criterio que para los artistas, si el usuario no está logueado no podrá visualizar sus datos.
    """
    if request.user.is_authenticated:
        information = get_information(request.user)
    else:
        information = {}

    # information = get_information(request.user)
    information['bandas'] = get_all_bandas()

    return render(
        request = request,
        template_name='Artistas/template_bandas.html',
        context= information
    )

@login_required(login_url='login/')
def render_view_formulario_bandas(request):
    """
    # Función para creación de bandas
    """
    if request.method == "POST":
        formulario = Banda_Formulario(request.POST)

        if formulario.is_valid:
            banda = Banda(
                nombre = request.POST['nombre'],
                historia_banda = request.POST['historia_banda']
            )
            banda.save()
            return redirect(render_view_bandas)
    else:
        formulario = Banda_Formulario()

    return render(request, 'Artistas/formulario_banda.html', {'form' : formulario})

@login_required(login_url='login/')
def render_view_update_bandas(request, id_banda = None):
    """
    # Función para actualizar bandas
    """
    if id_banda == None:
        return redirect(render_view_bandas)

    try:
        banda = Banda.objects.get(id = id_banda)
    except:
        return redirect(render_view_bandas)

    if request.method == "POST":
        formulario = Banda_Formulario(request.POST)
        if formulario.is_valid:
            banda.nombre = request.POST['nombre']
            banda.historia_banda = request.POST['historia_banda']
            
            try:
                create_or_update_banda(banda=banda)
                return redirect(render_view_bandas)
            except:
                return redirect(render_view_bandas)
    else:
        formulario = Banda_Formulario(instance=banda)

    return render(request, 'Artistas/formulario_update_banda.html', {'form' : formulario})

@login_required(login_url='login/')
def view_delete_banda(request, id_banda = None):
    """
    # Función para actualizar bandas
    """
    if id_banda == None:
        return redirect(render_view_bandas)

    try:
        banda = Banda.objects.get(id = id_banda)
    except:
        return redirect(render_view_bandas)

    if request.method == "GET":
            
        try:
            delete_banda(banda=banda)
            return redirect(render_view_bandas)
        except:
            return redirect(render_view_bandas)

@login_required(login_url='login/')
def render_view_formulario_artistas(request):
    """
    # Función para la creación de artistas
    """
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
    """
    # Formulario para editar artistas
    # Debe enviarse la id en la url
    """
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