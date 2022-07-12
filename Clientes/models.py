from Base.models import Persona, PersonaMixin, Base
from django.db import models    

ESTADOS = (
    (1, "ACTIVO"), 
    (2, "BAJA"), 
    (3, "MOROSO"),
)

class Cliente(PersonaMixin):
    id_number = models.CharField(max_length=50, unique=True, null=False)
    estado = models.CharField(max_length=50, choices=ESTADOS, default="ACTIVO", null=False)

    def __getitem__(self, key):
        return self.__dict__[key]
        # try:
        #     return self.__dict__[key]
        # except IndexError:
        #     return {}