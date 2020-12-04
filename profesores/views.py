from .models import Profesor
from .serializers import ProfesorSerializer

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

class Profesores(generics.ListCreateAPIView):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
   permission_classes = (AllowAny, )
       
class Teacher(generics.RetrieveUpdateDestroyAPIView):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
   permission_classes = (AllowAny, )

#4ta forma
class TeacherViewSet(viewsets.ModelViewSet):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
   permission_classes = (AllowAny, )
