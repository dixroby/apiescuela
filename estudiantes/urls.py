from django.urls import path
from .views import Estudiantes,Student, StudentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
""" path('', Estudiantes.as_view()), """
urlpatterns = [
    
    path('<int:pk>', Student.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = DefaultRouter()
router.register(r'', StudentViewSet)

urlpatterns += router.urls