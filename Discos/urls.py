from django.urls import path
from Discos.views import *

urlpatterns = [
    # Read
    path('', Discoslist.as_view(), name="discos-list"),
    path('<pk>', Discosdetalle.as_view(), name='discos-detail'),

    # Create
    path('formulariodisco/', formulario_disco, name='discosformulario'),
    
    # Delete
    path('eliminardisco/', eliminar_disco, name='eliminardisco'),

    # Update
    path('editar/<pk>', Editardiscos.as_view(), name='disco_editar'),

    # TODO: Ordenar los de abajo
    path('busquedadiscos/', busqueda_discos),
    path('buscar/', buscar),
    
]