from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from MainApp.views import paginaPrincipal
from Persona.views import getEstudiantes, nuevoEstudiante, gestionarEstudiante, getProfesores, gestionarProfesor, nuevoProfesor, eliminarPersona
from Curso.views import getCursos, gestionarCurso, nuevoCurso, eliminarCurso
from EstudiantesCursos.views import getEstudiantesCursos, gestionarEstudianteCurso, nuevoEstudianteCurso,eliminarEstudianteCurso
from Matriculas.views import getMatricula, nuevaMatricula, eliminarMatricula, gestionarMatricula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaPrincipal, name='paginaPrincipal'),
    path('lista-estudiantes/', getEstudiantes, name='listaEstudiantes'),
    path('add-estudiante/', nuevoEstudiante, name='addEstudiante'),
    path('editar-estudiante/<int:id>/', gestionarEstudiante, name='editarEstudiante'),
    path('lista-estudiantes/<int:id>/', eliminarPersona, name='eliminarPersona'),
    path('lista-profesores/', getProfesores, name='listaProfesores'),
    path('add-profesor/', nuevoProfesor, name='addProfesor'),
    path('editar-profesor/<int:id>/', gestionarProfesor, name='editarProfesor'),
    path('lista-profesores/<int:id>/', eliminarPersona, name='eliminarPersona'),
    path('lista-cursos/', getCursos, name='listaCursos'),
    path('add-curso/', nuevoCurso, name='addCurso'),
    path('editar-curso/<int:id>', gestionarCurso, name='editarCurso'),
    path('lista-cursos/<int:id>', eliminarCurso, name='eliminarCurso'),
    path('lista-estudiantes-cursos/', getEstudiantesCursos, name='listaEstudiantesCursos'),
    path('add-estudiante-curso/', nuevoEstudianteCurso, name='addEstudianteCurso'),
    path('editar-estudiante-curso/<int:id>/', gestionarEstudianteCurso, name='editarEstudianteCurso'),
    path('lista-estudiantes-cursos/<int:id>/', eliminarEstudianteCurso, name='eliminarEstudianteCurso'),
    path('lista-matriculas/', getMatricula, name='listaMatriculas'),
    path('editar-matricula/<int:id>', gestionarMatricula, name='editarMatricula'),
    path('lista-matriculas/<int:id>', eliminarMatricula, name='eliminarMatricula'),
    path('add-matricula/', nuevaMatricula, name='addMatricula'),
]
