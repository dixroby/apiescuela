from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class Estudiante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.CharField(max_length=8)
    activo = models.BooleanField(null=True)
    f_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.nombre