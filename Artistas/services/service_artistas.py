from Artistas.dtos.dto_artista import DTO_Artista_Extended
from Base.exceptions import BaseEntityNotFoundError
from ..models import Artista
from Discos.models import Discos


def get_all_artistas():
    return Artista.objects.all()

def get_artista(id):
    try:
        return Artista.objects.get(id = id)
    except:
        raise BaseEntityNotFoundError('Artista no encontrado')

def get_artista_por_nombre_y_apellido(nombre, apellido):
    return Artista.objects.filter(nombre = nombre).filter(appelido = apellido)

def get_discos_y_bandas_por_artista(artista: int):
    artista = Artista.objects.get(id = artista)
    banda = artista.banda

    discos = Discos.objects.filter(banda = banda.id)
    return discos


