from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from MainApp.views import paginaPrincipal
from Persona.views import getEstudiantes, nuevoEstudiante, gestionarEstudiante, getProfesores, gestionarProfesor, nuevoProfesor
from Curso.views import getCursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaPrincipal, name='paginaPrincipal'),
    path('lista-estudiantes/', getEstudiantes, name='listaEstudiantes'),
    path('add-estudiante/', nuevoEstudiante, name='addEstudiante'),
    path('editar-estudiante/<int:id>', gestionarEstudiante, name='editarEstudiante'),
    path('lista-profesores/', getProfesores, name='listaProfesores'),
    path('add-profesor/', nuevoProfesor, name='addProfesor'),
    path('editar-profesor/<int:id>', gestionarProfesor, name='editarProfesor'),
    path('lista-cursos/', getCursos, name='listaCursos'),
]
