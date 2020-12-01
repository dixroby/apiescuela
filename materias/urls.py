from django.urls import path
from .views import Materias,Curse

urlpatterns = [
    path('', Materias.as_view()),
    path('<int:pk>', Curse.as_view()),
]
    