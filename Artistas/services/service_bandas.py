from ..models import Banda

def get_all_bandas():
    return Banda.objects.all()