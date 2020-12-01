from rest_framework import serializers
from estudiantes.serializers import EstudianteSerializer
from profesores.serializers import ProfesorSerializer

from materias.models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    #relacion de muchos a muchos (read_only=True, many=True)
    estudiante = EstudianteSerializer(read_only=True, many=True)
    #relacion de uno a muchos (read_only=True) 
    profesor = ProfesorSerializer(read_only=True) 
    class Meta :
        model = Materia
        fields = '__all__'