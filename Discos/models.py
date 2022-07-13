from django.db import models
from Base.models import Base

# Create your models here.

class Disco(Base):
    nombre=models.CharField(max_length=50)
    year=models.IntegerField()
    duration=models.DurationField()

class Genero():
    





