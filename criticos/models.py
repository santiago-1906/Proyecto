from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Critico(models.Model):
    nombre = models.CharField(max_length=100)
    
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    bio = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"