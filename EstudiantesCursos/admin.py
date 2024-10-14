from django.contrib import admin
from EstudiantesCursos.models import EstudiantesCursos

# Register your models here.
@admin.register(EstudiantesCursos)
class EstudiantesCursosAdmin(admin.ModelAdmin):
    list_display = ('id', "estudiante_id", "curso_id", "fecha_inicio", 'fecha_fin', 'estado', 'nota_final');
    list_filter = ('estado',)