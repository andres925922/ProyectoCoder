from django.urls import path
from Discos.views import guardar_discos

urlpattern= [
    path('Discos/', guardar_discos, name=guardar_discos),


]