from django.db import models

# Create your models here.
class Eventos(models.Model):
    codigo = models.TextField(max_length=10)
    nombre_evento = models.TextField(max_length=200)
    fecha_evento = models.DateField()
    descripcion = models.TextField(max_length=300)
