from django.db import models
from Base.models import Base

# Create your models here.

class Genero(Base):
    descripcion = models.CharField(max_length=75, null=False)