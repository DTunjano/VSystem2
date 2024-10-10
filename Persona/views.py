from django.shortcuts import render, redirect # type: ignore
from .models import Persona

# Create your views here.
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

