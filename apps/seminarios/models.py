from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Seminario(models.Model):
    Nombre = models.CharField(max_length=50)
    Expositor = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Organizador = models.CharField(max_length=30)
    Lugar = models.CharField(max_length=60)
    Fecha = models.DateField()

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.Nombre, self.Expositor)
