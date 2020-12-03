from rest_framework import status, generics
from .models import Profesor
from .serializers import ProfesorSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

class Profesores(generics.ListCreateAPIView):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
   permission_classes = (AllowAny, )
       
class Teacher(generics.RetrieveUpdateDestroyAPIView):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
   permission_classes = (AllowAny, )