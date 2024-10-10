from django.contrib import admin # type: ignore
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id',"nombre", "capacidad_maxima", "profesor");
