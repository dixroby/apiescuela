from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admins/', admin.site.urls),
    path('estudiantes/', include('estudiantes.urls')),
    path('materias/', include('materias.urls')),
    path('profesores/', include('profesores.urls')),
]
