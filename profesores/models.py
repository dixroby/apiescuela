from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    edad = models.IntegerField(null=True)
    activo = models.BooleanField(null=True)
    f_nacimiento = models.DateField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.nombre