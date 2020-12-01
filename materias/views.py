from rest_framework import status, generics

from .models import Materia
from .serializers import MateriaSerializer
from rest_framework.views import APIView

class Materias(generics.ListCreateAPIView):
   queryset = Materia.objects.all()
   serializer_class = MateriaSerializer

class Curse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer