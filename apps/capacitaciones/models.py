from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Detalle = models.TextField(max_length=200, null=True, blank=True)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        if self.Estado:
            habilitado = "✓"
        else:
            habilitado = "X"
        cadena = "{0} ({1})"
        return cadena.format(self.Nombre, habilitado)

class Matricula(models.Model):
    Capacitador = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.Capacitador, self.Curso)