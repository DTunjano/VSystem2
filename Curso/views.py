from django.shortcuts import render # type: ignore
from .models import Curso

def getCursos(request):
    cursos = Curso.objects.all()

    return render(request, 'lista-cursos.html',{
        'title': 'Lista de cursos',
        'cursos': cursos
    })
