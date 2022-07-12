from django.db import models

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


class PersonaMixin(Persona):
    identity = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField()
    sexo = models.CharField(max_length=50, choices=SEXO)
    tel = models.CharField(max_length=50)
