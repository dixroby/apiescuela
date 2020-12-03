from rest_framework import serializers

from estudiantes.models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    materias = serializers.StringRelatedField(read_only=True, many=True)
    #materias = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #materias = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    materias = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta :
        model = Estudiante
        fields = '__all__'
        #fields = ('nombre','direccion',)