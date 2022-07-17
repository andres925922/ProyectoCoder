from django.http import HttpResponse
from django.shortcuts import render

from Clientes.models import Cliente
from .services.service_cliente import Servicio_Cliente as SC
from .forms.form_cliente import Formulario_Cliente, Formulario_Busqueda_cliente

# Create your views here.

service_cliente = SC()

def render_view_clientes(request):
    return render(
        request=request, 
        template_name='Clientes/template_clientes.html', 
        context={'clientes': service_cliente.get_all_clientes()}
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
        print(form)
        if form.is_valid:
            info = form.cleaned_data
            data = Cliente(
                id_number = info["id_number"],
                nombre = info["nombre"],
                apellido = info["apellido"],
                identity = info["identity"],
                email = info["email"],
                sexo = info["sexo"],
                tel = info["tel"],
                estado = info["estado"] )
            data.save()
            return render_view_clientes(request=request)
    else:
        form = Formulario_Cliente()
    
    return render(request, 'Clientes/form_cliente.html', 
    {
        "form" : form,
        "title": "Alta de clientes"
    })
