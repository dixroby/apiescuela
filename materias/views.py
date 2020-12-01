from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Materia
from estudiantes.models import Estudiante
from profesores.models import Profesor
from .serializers import MateriaSerializer
from rest_framework.views import APIView

class Materias(generics.ListCreateAPIView):
   queryset = Materia.objects.all()
   serializer_class = MateriaSerializer

class Curse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    """ this is comentary """
   
"""     def get(self, request,id):
        materia_obj = Materia.objects.get(id = id)
        serialized = MateriaSerializer(materia_obj)
        return Response(status = status.HTTP_200_OK,data= serialized.data ) 

    def put (self, request,id):
        materia_obj = Materia.objects.get(id = id)
        serialized = MateriaSerializer(instance = materia_obj,data=request.data,partial = True)
        
        if serialized.is_valid():
            serialized.save()            
            return Response(status = status.HTTP_200_OK,data= {"mensaje": "actualizado", **serialized.data})
        else :
            return Response(status = status.HTTP_400_BAD_REQUEST,data = serialized.errors)
        
    def delete (self, request,id):
        materia_obj = Materia.objects.get(id = id)
        materia_obj.delete()
        messaje = {
            "mensaje":"Estudiante "+materia_obj.nombre +" Eliminado"
        }
        return Response(status = status.HTTP_204_NO_CONTENT,data=messaje.data) """