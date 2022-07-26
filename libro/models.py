from django.db import models
from autor.models import Autor

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)  

    def __str__(self) -> str:
        return self.nombre

        
class Libro(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models. ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('fecha de lanzamiento')
    portada = models.ImageField(upload_to='portadas')
    visitas = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.titulo