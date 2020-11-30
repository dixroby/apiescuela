from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.CharField(max_length=8)
    activo = models.BooleanField(null=True)
    f_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.nombre