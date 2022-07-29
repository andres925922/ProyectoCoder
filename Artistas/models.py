from django.db import models
from Base.models import Base
from Clientes.models import Persona

# Create your models here.
class Banda(Base):
    nombre = models.CharField(max_length=100, unique=True)
    # genero

    def __str__(self) -> str:
        return self.nombre

class Artista(Persona):
    nombre_artistico = models.CharField(max_length=50, null=True, unique=True)
    banda = models.ForeignKey(Banda, on_delete=models.SET_NULL, null=True)
    historia = models.TextField(null=False, default='')
    # banda = models.ManyToManyField(
    #     Banda, 
    #     through='Artista_Banda', 
    #     through_fields=('artista', 'banda'),
    # )
    def __str__(self) -> str:
        return f"{self.nombre_artistico} - {self.nombre} {self.apellido}"

    class Meta: 
        unique_together = [ ["nombre", "apellido"] ]


# class Artista_Banda(Base):
#     artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
#     banda = models.ForeignKey(Banda, on_delete=models.CASCADE)


