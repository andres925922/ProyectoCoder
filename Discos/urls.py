from django.urls import path
from Discos.views import render_view_discos


urlpattern= [
    path('Discos/', render_view_discos),
    path('formulario_disco/', 'formulario_discos.html'),




]