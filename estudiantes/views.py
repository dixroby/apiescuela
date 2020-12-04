from .models import Estudiante
from .serializers import EstudianteSerializer
from materias.serializers import MateriaSerializer

from materias.models import Materia

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

# primera forma de generar POST, GET
class Estudiantes(generics.ListCreateAPIView):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer
   #permission_classes = [IsAuthenticated] or use permission_classes = [AllowAny] or use
   permission_classes = (AllowAny, )
       
# GET, PUT y DELETE de un estudiante
class Student(generics.RetrieveUpdateDestroyAPIView):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer

#Segunda forma de hacer lo anterior
class StudentViewSet(viewsets.ModelViewSet):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer
   permission_classes = (AllowAny, )
   
   @action(methods=['GET'], detail=True)
   def materia(self, request, pk=None):
      estudiante = self.get_object()
      curse = Materia.objects.filter()
      serializer = MateriaSerializer(estudiante.materia, many=True)
      return Response(status=status.HTTP_200_OK, data=serializer.data)

   @action(methods=['GET'], detail=True)
   def eliminar(self, request, pk=None):
      estudiante = self.get_object()
      estudiante.activo = not estudiante.activo
      estudiante.save()
      if estudiante.activo :
         data = {
            "mensaje":"estudiante "+estudiante.nombre +" ha sido habilitado"
         }
      else :
         data = {
            "mensaje":"estudiante "+estudiante.nombre +" ha sido deshabilitado"
         }
      return Response(status=status.HTTP_200_OK, data=data)
   
   @action(methods=['GET','POST','DELETE'], detail=True)
   def cursos(self, request, pk=None):
      estudiante = self.get_object()

      if request.method == 'GET':
         serializer = EstudianteSerializer(estudiante.materias, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)
      
      """ if request.method == 'POST':
         estudiantes_id = request.data['estudiantes_ids']

         for estudiante_id in estudiantes_id :
            estudiante = Estudiante.objects.get(id=estudiante_id) 
            curso.estudiante.add(estudiante)
         serializer = EstudianteSerializer(curso.estudiante, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data) """