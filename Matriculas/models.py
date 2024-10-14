from django.db import models
from EstudiantesCursos.models import EstudiantesCursos

# Create your models here.
class Matricula(models.Model):

    estudianteCurso_id = models.ForeignKey(EstudiantesCursos, verbose_name=("ID de EstudianteCurso"), on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    costo = models.FloatField()

    class Meta:
        verbose_name = ("Matricula")
        verbose_name_plural = ("Matriculas")

    def __str__(self):
        return f'{self.estudianteCurso_id}'
