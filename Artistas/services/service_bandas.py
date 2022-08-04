from Base.exceptions import BaseEntityNotFoundError, EntityCouldNotBeenCreated, EntityCouldNotBeenDeletedError
from ..models import Banda

def get_all_bandas():
    return Banda.objects.filter(deleted = False)

def get_banda(pk):
    try:
        return Banda.objects.get(pk=pk)
    except:
        raise BaseEntityNotFoundError('Banda no encontrada')

def create_or_update_banda(banda: Banda):
    try:
        banda.save()
    except:
        raise EntityCouldNotBeenCreated('Banda no creada')

def delete_banda(banda: Banda):
    try:
        banda.deleted = True
        banda.save()

    except:
        raise EntityCouldNotBeenDeletedError('Banda no eliminada')

