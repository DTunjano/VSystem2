from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from MainApp.views import paginaPrincipal
from Persona.views import getEstudiantes, nuevoEstudiante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaPrincipal, name='paginaPrincipal'),
    path('lista-estudiantes', getEstudiantes, name='listaEstudiantes'),
    path('add-estudiante', nuevoEstudiante, name='addEstudiante')
]
