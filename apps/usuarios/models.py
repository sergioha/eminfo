from django.db import models

# Create your models here.

class Login(models.Model):
    Usuario = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=128)

    def __str__(self):
        return self.Login

class Rol(models.Model):
    Rol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.Rol

class Usuario(models.Model):
    ApellidoPaterno = models.CharField(max_length=30)
    ApellidoMaterno = models.CharField(max_length=30)
    Nombres = models.CharField(max_length=30)
    Titulos = (('Est.','Estudiante'), ('Sr.','Señor'), ('Sra.','Señora'), ('Ing.','Ingeniero(a)'), ('Lic.','Licenciado(a)'), ('Arq.','Arquitecto(a)'), ('Dr.','Doctor'), ('Dra.','Doctora'), ('Mtr.','Master'))
    Titulo = models.CharField(max_length=5, choices=Titulos, default='Est.')
    CI = models.CharField(max_length=10, unique=True)
    Correo = models.EmailField(max_length=50, unique=True)
    Telefono = models.CharField(max_length=20)
    Login = models.OneToOneField(Login, null=False, blank=False, on_delete=models.CASCADE)
    Rol = models.ForeignKey(Rol, null=False, blank=False, on_delete=models.CASCADE)

    def NombreCompleto(self):
        cadena = "{0} {1} {2} {3}"
        return cadena.format(self.Titulo, self.Nombres, self.ApellidoPaterno, self.ApellidoMaterno)

    def __str__(self):
        return self.NombreCompleto()