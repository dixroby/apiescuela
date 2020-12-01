from rest_framework import status, generics
from .models import Profesor
from .serializers import ProfesorSerializer
from rest_framework.views import APIView

class Profesores(generics.ListCreateAPIView):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer
       
class Teacher(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    
