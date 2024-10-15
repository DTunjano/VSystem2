from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Persona

# Estudiantes
def getEstudiantes(request):
    estudiantes = Persona.objects.filter(rol = 'Estudiante')

    return render(request, 'lista-estudiantes.html',{
        'title': 'Lista de estudiantes',
        'estudiantes': estudiantes
    })

def nuevoEstudiante(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre_input')
        apellido = request.POST.get('apellido_input')
        dni = request.POST.get('dni_input')
        telefono = request.POST.get('telefono_input')
        email = request.POST.get('email_input')
        fecha_nacimiento = request.POST.get('fecha_nacimiento_input')

        
        nuevo_estudiante = Persona(
            nombre = nombre,
            apellido = apellido,
            dni = dni,
            telefono = telefono,
            email = email,
            fecha_nacimiento = fecha_nacimiento,
            rol = 'Estudiante'
        )

        nuevo_estudiante.save()

        return redirect('listaEstudiantes')

    return render(request, 'add-estudiante.html', {
        'title': 'Agregar nuevo estudiante'
        })

def gestionarEstudiante(request, id):
    estudiante = get_object_or_404(Persona, id=id)

    if(request.method == 'POST'):
        estudiante.nombre = request.POST.get('nombre_input')
        estudiante.apellido = request.POST.get('apellido_input')
        estudiante.dni = request.POST.get('dni_input')
        estudiante.telefono = request.POST.get('telefono_input')
        estudiante.email = request.POST.get('email_input')
        estudiante.fecha_nacimiento = request.POST.get('fecha_nacimiento_input')
        estudiante.save()

        return redirect('listaEstudiantes')

    return render(request, 'editar-estudiante.html', {
        'title': 'Información del estudiante',
        'estudiante': estudiante
        })

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, id=id)
    
    persona.delete()

    if persona.rol == 'Profesor':
        return redirect('listaProfesores')

    return redirect('listaEstudiantes')

#Profesores
def getProfesores(request):
    profesores = Persona.objects.filter(rol = 'Profesor')

    return render(request, 'lista-profesores.html',{
        'title': 'Lista de Profesores',
        'profesores': profesores
    })

def nuevoProfesor(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre_input')
        apellido = request.POST.get('apellido_input')
        dni = request.POST.get('dni_input')
        telefono = request.POST.get('telefono_input')
        email = request.POST.get('email_input')
        fecha_nacimiento = request.POST.get('fecha_nacimiento_input')

        
        nuevo_profesor = Persona(
            nombre = nombre,
            apellido = apellido,
            dni = dni,
            telefono = telefono,
            email = email,
            fecha_nacimiento = fecha_nacimiento,
            rol = 'Profesor'
        )

        nuevo_profesor.save()

        return redirect('listaProfesores')

    return render(request, 'add-profesor.html', {
        'title': 'Agregar nuevo profesor'
        })

def gestionarProfesor(request, id):
    profesor = get_object_or_404(Persona, id=id)

    if(request.method == 'POST'):
        profesor.nombre = request.POST.get('nombre_input')
        profesor.apellido = request.POST.get('apellido_input')
        profesor.dni = request.POST.get('dni_input')
        profesor.telefono = request.POST.get('telefono_input')
        profesor.email = request.POST.get('email_input')
        profesor.fecha_nacimiento = request.POST.get('fecha_nacimiento_input')
        profesor.save()

        return redirect('listaProfesores')

    return render(request, 'editar-profesor.html', {
        'title': 'Información del Profesor',
        'profesor': profesor
        })
