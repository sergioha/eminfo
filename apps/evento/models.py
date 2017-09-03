from django.db import models

# Create your models here.
class Evento(models.Model):
    Codigo = models.CharField(max_length=20,unique=True,null=False)
    Nombre = models.CharField(max_length=50,null=False)
    Fecha_inicio = models.DateField(null=True)
    Fecha_Fin = models.DateField(null=True)
    Encargado=models.CharField(null=True,max_length=50)
    Descripcion = models.TextField(max_length=300,null=True)
    def __str__(self):
       # return '{}'.format(self.Nombre),format(self.Fecha_inicio)
       return '%s %s' % (self.Nombre, self.Fecha_inicio)
         # return self.Nombre
        






class Meta:
        ordering = ["Nombre"]
        db_table = 'evento'