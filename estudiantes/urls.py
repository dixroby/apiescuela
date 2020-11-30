from django.urls import path
from .views import Estudiantes,Student

urlpatterns = [
    path('', Estudiantes.as_view()),
    path('<int:id>', Student.as_view()),
]