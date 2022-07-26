from django.db import models
from libro.models import Libro

        
class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models. CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellidos}'

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    def __str__(self) -> str:
        return self.libro.titulo
