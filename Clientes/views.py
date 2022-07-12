from django.shortcuts import render
from .services.service_cliente import Servicio_Cliente as SC

# Create your views here.

service_cliente = SC()

def render_view_clientes(request):
    return render(
        request=request, 
        template_name='Clientes/template_clientes.html', 
        context={'clientes': service_cliente.get_all_clientes()}
    )
