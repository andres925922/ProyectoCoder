from django.urls import path
from Discos.views import *


urlpattern= [
    path('Discos/', render_view_discos, name=Discos),
    path('formulario_disco/', 'formulario_discos.html'),




]