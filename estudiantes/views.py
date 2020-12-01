from rest_framework import status, generics
from .models import Estudiante
from .serializers import EstudianteSerializer
from rest_framework.views import APIView

class Estudiantes(generics.ListCreateAPIView):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer
       

class Student(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer