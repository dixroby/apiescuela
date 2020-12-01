from django.urls import path
from .views import Profesores,Teacher

urlpatterns = [
    path('', Profesores.as_view()),
    path('<int:pk>', Teacher.as_view()),
]
