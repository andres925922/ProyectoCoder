from django.urls import path
from Discos.views import *


# /discos/ -> lista todos los discos
# /discos/1 -> muestra el disco con id 1

urlpatterns = [
    # path('', render_view_discos, name="ver_discos"),
    path('formulariodisco/', formulario_disco, name='discosformulario'),
    path('busquedadiscos/', busqueda_discos),
    path('buscar/', buscar),
    path('', Discoslist.as_view(), name="ver_discos"),
    path('eliminardisco/', eliminar_disco, name='eliminardisco'),
    path('editar/<pk>', Editardiscos.as_view(), name='disco_editar'),
    path('detalles/<pk>', Discosdetalle.as_view, name='detallediscos'),
    path('test/', test_view)
]