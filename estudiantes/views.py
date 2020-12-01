from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Estudiante
from .serializers import EstudianteSerializer
from rest_framework.views import APIView

class Estudiantes(generics.ListCreateAPIView):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer
       

class Student(APIView):
    """ this is comentary """
   
    def get(self, request,id):
        libro_objt =Estudiante.objects.get(id = id)
        serialized = EstudianteSerializer(libro_objt)
        return Response(status = status.HTTP_200_OK,data= serialized.data ) 

    def put (self, request,id):
        estudiante_bjto = Estudiante.objects.get(id = id)
        serialized = EstudianteSerializer(instance = estudiante_bjto,data=request.data,partial = True)
        messaje = {
            "mensaje":"Estudiante "+estudiante_bjto.nombre +" Actualizado"
        }
        if serialized.is_valid():
            serialized.save()
            return Response(status = status.HTTP_200_OK,data = serialized.data)
        else :
            return Response(status = status.HTTP_400_BAD_REQUEST,data = serialized.errors)
        
    def delete (self, request,id):
        estudiante_bjto = Estudiante.objects.get(id = id)
        estudiante_bjto.delete()
        messaje = {
            "mensaje":"Estudiante "+estudiante_bjto.nombre+estudiante_bjto.apellidos +" Eliminado"
        }
        return Response(status = status.HTTP_204_NO_CONTENT,data=messaje)