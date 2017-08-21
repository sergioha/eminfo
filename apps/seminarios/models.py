from django.db import models

# Create your models here.

class Expositor(models.Model):
    ApellidoPaterno = models.CharField(max_length=30)
    ApellidoMaterno = models.CharField(max_length=30)
    Nombres = models.CharField(max_length=30)
    Titulos = (('Sr.','Señor'), ('Sra.','Señora'), ('Ing.','Ingeniero(a)'), ('Lic.','Licenciado(a)'), ('Arq.','Arquitecto(a)'), ('Dr.','Doctor'), ('Dra.','Doctora'), ('Mtr.','Master'))
    Titulo = models.CharField(max_length=5, choices=Titulos, default='Sr.')
    CI = models.CharField(max_length=10)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=20)

    def NombreCompleto(self):
        cadena = "{0} {1} {2} {3}"
        return cadena.format(self.Titulo, self.Nombres, self.ApellidoPaterno, self.ApellidoMaterno)

    def __str__(self):
        return self.NombreCompleto()

class Seminario(models.Model):
    Nombre = models.CharField(max_length=50)
    Expositor = models.ForeignKey(Expositor, null=False, blank=False, on_delete=models.CASCADE)
    Organizador = models.CharField(max_length=30)
    Lugar = models.CharField(max_length=60)
    Fecha = models.DateField()

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.Nombre, self.Expositor)
