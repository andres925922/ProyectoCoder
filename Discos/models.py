from django.db import models
from Base.models import Base

# Create your models here.

class Discos(Base):
    nombre=models.CharField(max_length=50)
    year=models.IntegerField()
    duration=models.DurationField()

class Genero(Base):
    nombre=models.CharField(max_length=50)
    
    





