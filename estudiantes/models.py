from django.db import models
import uuid

class Estudiante(models.Model):
    id = models.UUIDField(default = uuid.uuid4,primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.CharField(max_length=8)
    activo = models.BooleanField(null=True)
    f_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.nombre