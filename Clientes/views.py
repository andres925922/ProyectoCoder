from django.http import HttpResponse
from django.shortcuts import render, redirect
from Base.exceptions import BaseEntityNotFoundError, EntityAlreadyCreatedError

from Base.services.base_service import get_about

from Clientes.models import Cliente
from .services.service_cliente import Servicio_Cliente as SC
from .forms.form_cliente import Formulario_Cliente, Formulario_Busqueda_cliente

# Create your views here.

service_cliente = SC()

def render_view_clientes(request):
    return render(
        request=request, 
        template_name='Clientes/template_clientes.html', 
        context={'clientes': service_cliente.get_all_clientes(), 
        'founders': get_about()
        }
    )

def render_buscar_cliente_por_dni(request):
    formulario = Formulario_Busqueda_cliente
    return render(
        request, 
        'Clientes/busqueda_cliente_por_dni.html',
        context= {
            "title": "Búsqueda de cliente por DNI",
            "form": formulario  
        })

def buscar_cliente_por_dni(request):
    print(request)
    cliente = service_cliente.get_cliente_por_dni(
        value = request.GET['dni']
    )
    print(cliente)
    if cliente:
        return HttpResponse(f"El cliente seleccionado es {cliente.nombre} {cliente.apellido}")
    else: 
        return HttpResponse("Cliente no encontrado")

def render_crear_cliente(request):
    if request.method == "POST":
        form = Formulario_Cliente(request.POST)
        if form.is_valid:
            # info = form.cleaned_data
            data = Cliente(
                id_number = request.POST["id_number"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                identity = request.POST["identity"],
                email = request.POST["email"],
                sexo = request.POST["sexo"],
                tel = request.POST["tel"],
                estado = request.POST["estado"] )
            try:
                service_cliente.crear_cliente(data)
                return redirect(render_view_clientes)
            except EntityAlreadyCreatedError as e:
                return HttpResponse(e)
            except Exception as e:
                return HttpResponse(e)
    else:
        form = Formulario_Cliente()
    
    return render(request, 'Clientes/form_cliente.html', 
    {
        "form" : form,
        "title": "Alta de clientes",
        "url": "/clientes/alta/"
    })

def render_actualizar_cliente(request, id_cliente = None):
    if request.method == "POST":
        form = Formulario_Cliente(request.POST)
        if form.is_valid:
            # info = form.cleaned_data
            data = Cliente(
                id_number = request.POST["id_number"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                identity = request.POST["identity"],
                email = request.POST["email"],
                sexo = request.POST["sexo"],
                tel = request.POST["tel"],
                estado = request.POST["estado"] )
            try:
                service_cliente.actualizar_cliente(data)
                return redirect(render_view_clientes)
            except Exception as e:
                print(e)
                return HttpResponse("Ha ocurrido un error al actualizar")
    else:
        try:
            cliente = service_cliente.get_cliente_por_numero_cliente(value=id_cliente)
            form = Formulario_Cliente(
                initial= {
                    "id_number" : cliente.numero_cliente,
                    "nombre" : cliente.nombre,
                    "apellido" : cliente.apellido,
                    "identity" : cliente.dni,
                    "email" : cliente.email,
                    "sexo" : cliente.sexo,
                    "tel" : cliente.tel,
                    "estado" : cliente.estado
                }
            )
        except:
            return HttpResponse("Ha ocurrido un error")
    
    return render(request, 'Clientes/form_cliente.html', 
    {
        "form" : form,
        "title": "Actualizar de clientes",
        "url": "/clientes/actualizar_cliente/"
    })

def render_eliminar_cliente(request, id_cliente = None):
    if id_cliente:
        try:
            service_cliente.eliminar_cliente(id_cliente=id_cliente)
        except BaseEntityNotFoundError:
            return HttpResponse("El número de cliente a eliminar no existe")
        except Exception as e:
            return HttpResponse(e)
    
    return redirect(render_view_clientes)

