from django.db import models
from estudiantes.models import Estudiante
from profesores.models import Profesor

class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ManyToManyField(Estudiante, related_name = 'materias') 

    
    def __str__(self):
        return self.nombre  