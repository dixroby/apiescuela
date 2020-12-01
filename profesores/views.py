from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profesor
from .serializers import ProfesorSerializer
from rest_framework.views import APIView

class Profesores(generics.ListCreateAPIView):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
       
class Teacher(APIView):
    """ this is comentary """
   
    def get(self, request,id):
        profe_obj =Profesor.objects.get(id = id)
        serialized = ProfesorSerializer(profe_obj)
        return Response(status = status.HTTP_200_OK,data= serialized.data ) 

    def put (self, request,id):
        profe_obj = Profesor.objects.get(id = id)
        serialized = ProfesorSerializer(instance = profe_obj,data=request.data,partial = True)
        messaje = {
            "mensaje":"Estudiante "+profe_obj.nombre +" Actualizado"
        }
        if serialized.is_valid():
            serialized.save()
            return Response(status = status.HTTP_200_OK,data = serialized.data)
        else :
            return Response(status = status.HTTP_400_BAD_REQUEST,data = serialized.errors)
        
    def delete (self, request,id):
        profe_obj = Profesor.objects.get(id = id)
        profe_obj.delete()
        messaje = {
            "mensaje":"Estudiante "+profe_obj.nombre+profe_obj.apellido +" Eliminado"
        }
        return Response(status = status.HTTP_204_NO_CONTENT,data=messaje)
    
