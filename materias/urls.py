from django.urls import path
from .views import Materias,Curse,CurseViewSet
from rest_framework.routers import DefaultRouter

#path('', Materias.as_view()),
urlpatterns = [    
    path('<int:pk>', Curse.as_view()),
]

router = DefaultRouter()
router.register(r'', CurseViewSet)

urlpatterns += router.urls    