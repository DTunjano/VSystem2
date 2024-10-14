from django.db import models
from django.core.exceptions import ValidationError # type: ignore
from Persona.models import Persona 
from Curso.models import Curso

class EstudiantesCursos(models.Model):
    estudiante_id = models.ForeignKey(
        Persona, 
        verbose_name= "ID del Estudiante", 
        on_delete=models.CASCADE,
        limit_choices_to={'rol':'Estudiante'}
        )
    curso_id = models.ForeignKey(Curso, verbose_name='ID del Curso', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False, verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(null=False, verbose_name='Fecha de finalización')
    estado = models.CharField(max_length=50, null=False)
    nota_final = models.FloatField(null=False,)

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def clean(self):
        if(self.nota_final < 0 or self.nota_final > 5):
            raise ValidationError('La nota final solo puede estar en un intervalo de 0.0 a 5.0')
        
        if(self.nota_final < 3 and self.estado == 'Aprobado'):
            raise ValidationError('El estado no puede ser aprobado si el estudiante tiene una nota menor a 3')

    def __str__(self):
        return f'{self.estudiante_id} {self.curso_id}'

    class Meta:
        db_table = 'EstudiantesCursos'
