from django.contrib import admin
from .models import Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('estudianteCurso_id', 'estado', 'fecha_inicio', 'costo')
    list_filter = ('estado',)