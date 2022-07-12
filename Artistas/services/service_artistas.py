from ..models import Artista


def get_all_artistas():
    return Artista.objects.all()

def get_artista_por_nombre_y_apellido(nombre, apellido):
    return Artista.objects.filter(nombre = nombre).filter(appelido = apellido)

