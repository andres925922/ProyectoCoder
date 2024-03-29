from django.db import models
from django.contrib import admin
from Artistas.models import Artista, Banda
from Base.models import Base

# Create your models here.

class Discos(Base):
    class Meta:
        # Cambia el nombre en plural con el que modelo discos aparece en el admin
        verbose_name_plural = "Discos"

    nombre=models.CharField(max_length=50)
    year=models.IntegerField()
    duration=models.DurationField()
    banda = models.ForeignKey(
        to= Banda, on_delete=models.PROTECT
    )
    portada = models.ImageField(upload_to='Discos', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class Genero(Base):
    nombre=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    def __getitem__(self, key):
        return self.__dict__[key]

class Canciones(Base):
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField(null=None)
    discos = models.ForeignKey(Discos, on_delete=models.PROTECT, null=False)
    bandas = models.ManyToManyField(
        Banda,
        through='Canciones_Banda'
    )
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, null=False)
    artistas = models.ManyToManyField(Artista,
    through='Canciones_Artista'
    )

    def __str__(self):
        return self.nombre
    
class Canciones_Banda(Base):
    cancion = models.ForeignKey(
        Canciones, on_delete=models.CASCADE, blank=True, null=False
    )
    banda = models.ForeignKey(
        Banda, on_delete=models.CASCADE, blank=True, null=False
    )

class Canciones_Artista(Base):
    cancion = models.ForeignKey(
        Canciones, on_delete=models.CASCADE, blank=True, null=False
    )
    artista = models.ForeignKey(
        Artista, on_delete=models.CASCADE, blank=True, null=False
    )

admin.site.register([Genero, Discos, Canciones])