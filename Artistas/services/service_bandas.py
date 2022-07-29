from Base.exceptions import BaseEntityNotFoundError
from ..models import Banda

def get_all_bandas():
    return Banda.objects.all()

def get_banda(pk):
    try:
        return Banda.objects.get(pk=pk)
    except:
        raise BaseEntityNotFoundError('Banda no encontrada')