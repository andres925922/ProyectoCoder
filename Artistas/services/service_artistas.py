from Artistas.dtos.dto_artista import DTO_Artista_Extended
from Base.exceptions import BaseEntityNotFoundError
from ..models import Artista
from Discos.models import Discos


def get_all_artistas():
    """
    # Servicio que retorna todos los artistas que se encuentran activos
    """
    return Artista.objects.filter(deleted = False)

def get_artista(id):
    """
    # Servicio que permite obtener la información de un artista en particular
    """
    try:
        return Artista.objects.get(id = id)
    except:
        raise BaseEntityNotFoundError('Artista no encontrado')

def get_artista_por_nombre_y_apellido(nombre, apellido):
    return Artista.objects.filter(nombre = nombre).filter(appelido = apellido)

def get_discos_y_bandas_por_artista(artista: int):
    """ 
    # artista: int
    # Servicio que permite obtener los discos de la banda a la cual pertenece el artista
    """
    artista = Artista.objects.get(id = artista)
    banda = artista.banda

    discos = Discos.objects.filter(banda = banda.id)
    return discos


