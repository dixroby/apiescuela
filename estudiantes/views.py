from rest_framework import status, generics
from .models import Estudiante
from .serializers import EstudianteSerializer
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, AllowAny

class Estudiantes(generics.ListCreateAPIView):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer
   #permission_classes = [IsAuthenticated] or use permission_classes = [AllowAny] or use
   #permission_classes = (AllowAny, )
       

class Student(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer