from django.db import models

from django.contrib import admin

# Create your models here.

class Base(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    created_at = models.DateField(auto_now_add=True, null= False)
    modificated_at = models.DateField(auto_now=True, null=False)
    deleted = models.BooleanField(default=False, null=False)

    class Meta:
        abstract = True


SEXO = ( (1, "FEMENINO"), (2, "MASCULINO"), )

class Persona(Base):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=75, null=False)

    class Meta:
        abstract = True

class PersonaMixin(Persona):
    identity = models.CharField(max_length=50, unique=True, null=False) # DNI
    email = models.EmailField()
    sexo = models.CharField(max_length=50, choices=SEXO)
    tel = models.CharField(max_length=50)

    class Meta:
        abstract = True

class About(Persona):
    description = models.TextField(max_length=300)
    img = models.ImageField(upload_to='aboutImg', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def __getitem__(self, key):
        return self.__dict__[key]



admin.site.register(About)

