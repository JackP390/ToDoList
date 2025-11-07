from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)