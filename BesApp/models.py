from django.db import models
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, EmailField, IntegerField
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, null=True)
    cantidad = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.nombre} {self.tipo}'

class Compras(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    cantidad = models.BooleanField(null=True)
    def __str__(self):
        return f'{self.nombre} {self.tipo}'


class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = models.ImageField(upload_to = 'avatares' , null=True, blank=True)

