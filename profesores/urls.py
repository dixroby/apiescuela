from django.urls import path
from .views import Profesores,Teacher,TeacherViewSet
from rest_framework.routers import DefaultRouter

""" urlpatterns = [
    path('', Profesores.as_view()),
    path('<int:pk>', Teacher.as_view()),
] """
router = DefaultRouter()
router.register(r'', TeacherViewSet)

urlpatterns = router.urls    