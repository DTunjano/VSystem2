from django.db import models # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from Persona.models import Persona


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_maxima = models.IntegerField(null=False)
    profesor = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
        
    def clean(self):

        if self.nombre == '':
            raise ValidationError('El nombre del curso no puede estar vacio')

        if self.capacidad_maxima <= 0:
            raise ValidationError('La capacidad máxima debe ser mayor a 0.')

        if self.profesor.rol != 'Profesor':
            raise ValidationError('Solo se pueden asiganar a profesores en este campo.')
        
    def __str__(self):
        return {self.nombre}

    class Meta:
        db_table = 'curso'