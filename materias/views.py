from .models import Materia
from .serializers import MateriaSerializer
from profesores.serializers import ProfesorSerializer
from estudiantes.serializers import EstudianteSerializer

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

class Materias(generics.ListCreateAPIView):
   queryset = Materia.objects.all()
   serializer_class = MateriaSerializer
   permission_classes = (AllowAny, )

class Curse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = (AllowAny, )

#segunda forma  de crear CRUD completo
class CurseViewSet(viewsets.ModelViewSet):
   queryset = Materia.objects.all()
   serializer_class = MateriaSerializer
   permission_classes = (AllowAny, )

   @action(methods=['GET'], detail=True)
   def estudiantes(self, request, pk=None):
      curso = self.get_object()
      serializer = EstudianteSerializer(curso.estudiante, many=True)
      return Response(status=status.HTTP_200_OK, data=serializer.data)

   @action(methods=['GET'], detail=True)
   def profesor(self, request, pk=None):
      curso = self.get_object()
      serializer = ProfesorSerializer(curso.profesor)
      return Response(status=status.HTTP_200_OK, data=serializer.data)
   