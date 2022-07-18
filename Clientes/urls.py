from django.urls import path
from .views import buscar_cliente_por_dni, render_actualizar_cliente, render_buscar_cliente_por_dni, render_crear_cliente, render_view_clientes

urlpatterns = [
    path('', render_view_clientes, name="all_clientes"),
    path('alta/', render_crear_cliente),
    path('actualizar_cliente/<id_cliente>', render_actualizar_cliente),
    path('actualizar_cliente/', render_actualizar_cliente),
    path('buscar_cliente_por_dni/', render_buscar_cliente_por_dni ),
    path('eliminar_cliente/<id_cliente>', render_buscar_cliente_por_dni ),
    path('buscar/', buscar_cliente_por_dni),
]