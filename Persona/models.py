from django.db import models # type: ignore

class Persona(models.Model):
    ROL_CHOICES = [
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
    
    class Meta:
        db_table='persona'
