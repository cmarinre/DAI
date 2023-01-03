# recetas/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_mayus(value):
  result = re.match('[A-Z]+.*', value)
  if result==None:
    raise ValidationError(
      _('%(value)s no empieza por mayúscula'),
      params={'value': value}
    )

def validate_mayusPreparacion(value):
  result = re.match('[A-Z]+.*', value)
  if result==None:
    raise ValidationError(
      _('El texto introducido no empieza por mayúscula'),
      params={'value': value}
    )

class Receta(models.Model):
  nombre       = models.CharField(max_length=200, validators=[validate_mayus])
  preparación  = models.TextField(max_length=5000, validators=[validate_mayusPreparacion])
  foto         = models.FileField(upload_to='media/fotos')
  ... 
  
  def __str__(self):
    return self.nombre
  
class Ingrediente(models.Model):
  nombre        = models.CharField(max_length=100)
  cantidad      = models.PositiveSmallIntegerField()
  unidades      = models.CharField(max_length=5)
  receta        = models.ForeignKey(Receta, on_delete=models.CASCADE)
  ...

  def __str__(self):
    return self.nombre