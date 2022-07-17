from django.db import models
from Base.models import Base
from Artistas.models import Artista
from Discos.models import Genero

# Create your models here.

class Canciones(Base):
    descripcion = models.CharField(max_length=100, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
