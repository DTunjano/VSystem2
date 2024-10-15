from django.shortcuts import render, redirect, get_object_or_404
from .models import EstudiantesCursos
from Persona.models import Persona
from Curso.models import Curso

def getEstudiantesCursos(request):
    est_x_cursos = EstudiantesCursos.objects.all()

    return render(request, 'lista-estudiantes-cursos.html',{
        'title': 'Lista de estudiantes por curso',
        'est_x_curso': est_x_cursos
    })

def gestionarEstudianteCurso(request, id):
    estudiante_curso = get_object_or_404(EstudiantesCursos, id=id)
    estudiantes = Persona.objects.filter(rol = 'Estudiante')
    cursos = Curso.objects.all()

    if(request.method == 'POST'):
        estudiante_id = request.POST.get('estudiante_id_input')
        if estudiante_id:
            estudiante = Persona.objects.get(id = int(estudiante_id))
            estudiante_curso.estudiante_id = estudiante

        curso_id = request.POST.get('curso_id_input')
        if curso_id:
            curso = Curso.objects.get(id = int(curso_id))
            estudiante_curso.curso_id = curso

        estudiante_curso.fecha_inicio = request.POST.get('fecha_inicio_input')
        estudiante_curso.fecha_fin = request.POST.get('fecha_fin_input')
        estudiante_curso.estado = request.POST.get('estado_input')
        estudiante_curso.nota_final = request.POST.get('nota_final_input')

        estudiante_curso.save()

        return redirect('listaEstudiantesCursos')
    
    context = {
        'estudiante_curso': estudiante_curso,
        'cursos': cursos,
        'estudiantes': estudiantes,
        'title': 'Informacion de estudiante por curso',
    }

    return render(request, 'editar-estudiante-curso.html', context)

def nuevoEstudianteCurso(request):
    estudiantes = Persona.objects.filter(rol = 'Estudiante')
    cursos = Curso.objects.all()
    estudiante_id = request.POST.get('estudiante_id_input')

    if estudiante_id:
        estudiante = Persona.objects.get(id = int(estudiante_id))

        curso_id = request.POST.get('curso_id_input')
        if curso_id:
            curso = Curso.objects.get(id = int(curso_id))

        fecha_inicio = request.POST.get('fecha_inicio_input')
        fecha_fin = request.POST.get('fecha_fin_input')
        estado = request.POST.get('estado_input')
        nota_final = request.POST.get('nota_final_input')

        nuevo_estudiante_curso = EstudiantesCursos(
            estudiante_id = estudiante,
            curso_id = curso,
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            estado = estado,
            nota_final = nota_final
        )

        nuevo_estudiante_curso.save()

        return redirect('listaEstudiantesCursos')
    
    context = {
        'cursos': cursos,
        'estudiantes': estudiantes,
        'title': 'Nuevo registro de estudiante por curso',
    }

    return render(request, 'add-estudiante-curso.html', context)

def eliminarEstudianteCurso(request, id):
    estudiante_curso = get_object_or_404(EstudiantesCursos, id=id)
    
    estudiante_curso.delete()

    return redirect('listaEstudiantesCursos')