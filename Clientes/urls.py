from django.urls import path
from .views import render_crear_cliente, render_view_clientes

urlpatterns = [
    path('', render_view_clientes),
    path('alta/', render_crear_cliente),
]