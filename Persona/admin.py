from django.contrib import admin # type: ignore
from Persona.models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "dni", "telefono", "email", "fecha_nacimiento", "rol")
    list_filter = ("rol",)
