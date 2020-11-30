from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    activo = models.BooleanField(null=True)
    f_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return self.nombre