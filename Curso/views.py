from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Curso
from Persona.models import Persona

def getCursos(request):
    cursos = Curso.objects.all()

    return render(request, 'lista-cursos.html',{
        'title': 'Lista de cursos',
        'cursos': cursos
    })

def gestionarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    profesores = Persona.objects.filter(rol = 'Profesor')

    if(request.method == 'POST'):
        curso.nombre = request.POST.get('nombre_input')
        curso.capacidad_maxima = request.POST.get('capacidad_maxima_input')

        profesor_id = request.POST.get('profesor_input')
        if profesor_id:
            profesor = Persona.objects.get(id=int(profesor_id))
            curso.profesor = profesor

        curso.save()

        return redirect('listaCursos')
    
    context = {
        'curso': curso,
        'profesores': profesores,
        'title': 'Informacion del curso',
    }

    return render(request, 'editar-curso.html', context)

def nuevoCurso(request):
    profesores = Persona.objects.filter(rol = 'Profesor')
    
    if request.method == 'POST':

        nombre = request.POST.get('nombre_input')
        capacidad_maxima = request.POST.get('capacidad_maxima_input')

        profesor_id = request.POST.get('profesor_input')
        if profesor_id:
            profesor = Persona.objects.get(id=int(profesor_id))


        
        nuevo_curso = Curso(
            nombre = nombre,
            capacidad_maxima = capacidad_maxima,
            profesor = profesor,
        )

        nuevo_curso.save()

        return redirect('listaCursos')

    return render(request, 'add-curso.html', {
        'title': 'Agregar nuevo curso',
        'profesores': profesores
        })

def eliminarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    
    curso.delete()

    return redirect('listaCursos')