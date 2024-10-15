from django.shortcuts import render, redirect, get_object_or_404
from .models import Matricula
from EstudiantesCursos.models import EstudiantesCursos

def getMatricula(request):
    matriculas = Matricula.objects.all()

    return render(request, 'lista-matriculas.html',{
        'title': 'Lista de matriculas',
        'matriculas': matriculas
    })

def gestionarMatricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    estudiantes_cursos = EstudiantesCursos.objects.all()

    if(request.method == 'POST'):
        estudiante_curso_id = request.POST.get('estudiante_curso_id_input')

        if estudiante_curso_id:
            estudiante_curso = EstudiantesCursos.objects.get(id = int(estudiante_curso_id))
            matricula.estudianteCurso_id = estudiante_curso

        matricula.estado = request.POST.get('estado_input')
        matricula.fecha_inicio = request.POST.get('fecha_inicio_input')
        matricula.costo = request.POST.get('costo_input')

        matricula.save()

        return redirect('listaMatricula')
    
    context = {
        'matricula': matricula,
        'estudiantes_cursos': estudiantes_cursos,
        'title': 'Informacion de la matricula',
    }

    return render(request, 'editar-matricula.html', context)

def nuevaMatricula(request):
    estudiantes_cursos = EstudiantesCursos.objects.all()
    
    if request.method == 'POST':
        
        estudiante_curso_id = request.POST.get('estudiante_curso_id_input')
        if estudiante_curso_id:
            estudiante_curso = EstudiantesCursos.objects.get(id = int(estudiante_curso_id))
        
        estado = request.POST.get('estado_input')
        fecha_inicio = request.POST.get('fecha_inicio_input')
        costo = request.POST.get('costo_input')


        
        nueva_matricula = Matricula(
            estudianteCurso_id = estudiante_curso,
            estado = estado,
            fecha_inicio = fecha_inicio,
            costo = costo
        )

        nueva_matricula.save()

        return redirect('listaMatriculas')

    return render(request, 'add-matricula.html', {
        'title': 'Agregar nueva matricula',
        'estudiantes_cursos': estudiantes_cursos
        })

def eliminarMatricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    
    matricula.delete()

    return redirect('listaMatriculas')
