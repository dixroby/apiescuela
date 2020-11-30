from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.CharField(max_length=8)
    edad = models.IntegerField(null=True)
    activo = models.BooleanField(null=True)
    f_nacimiento = models.DateField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.nombre