from django.db import models
from django.contrib.auth.models import User
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre= models.CharField(max_length=256, default='Mi nombre...')
    Direccion = models.CharField(max_length=256, default='Mi dirección...')
    Pais = models.CharField(max_length=256, default='Mi país...')
    Nacimiento = models.CharField(max_length=256, default='Mi fecha de nacimiento...')
    Edad = models.CharField(max_length=256, default='Mi edad...')
    Dni = models.CharField(max_length=256, default='Mi D.N.I...')
    Email = models.CharField(max_length=256, default='Mi correo electrónico...')
    Telefono = models.CharField(max_length=256, default='Mi número...')
    EducacionPrimaria = models.CharField(max_length=256, default='Mi Educacíon primaria...')
    EducacionSecundaria = models.CharField(max_length=256, default='Mi Educacíon secundaria...')
    EducacionOtro = models.CharField(max_length=256, default='Mi Educacíon orientada...')
    EducacionDeImportancia = models.CharField(max_length=256, default='Otros estudios...')
    OtrosConocimientos = models.CharField(max_length=256, default='Otros conocimentos...')
    IdiomaNativo = models.CharField(max_length=256, default='mi idioma...')
    IdiomaSecundario = models.CharField(max_length=256, default='Idioma...')
    IdiomaTerciario = models.CharField(max_length=256, default='Idioma...')
    Informatica = models.CharField(max_length=256, default='Conocimientos de Informática...')
    EspectativaDePuesto = models.CharField(max_length=256, default='Espectativa de puesto...')
    ExperienciaLaboral = models.CharField(max_length=256, default='Mis experiencias laborales...')
    DiasInscripto = models.DateTimeField(auto_now_add=True)
    FechaDeLaUltimaEdicion = models.DateTimeField(auto_now_add=True)
    MostrarCV = models.BooleanField(default=True)
    CuentaPaga = models.BooleanField(default=False)
    FechaDeCreacion = models.DateTimeField(auto_now_add=True)

class Flyers(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, default='Agregar una Imagen')

class Diplomas(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, default='Agregar un Diploma')

class PaginasWeb(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, default='Agregar una Web')

class DatosUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.OneToOneField(User, on_delete=models.CASCADE)
    FotoDePerfil = models.CharField(max_length=256, default='Agregar un Link')
    FotoDePortada = models.CharField(max_length=256, default='Agregar un Link')
    NumeroDeTelefono = models.CharField(max_length=256, default='Mi número...')
    DeQueTrabajo = models.CharField(max_length=256, default='Traba de..')
    SegundoFactorDeAutentificacion = models.BooleanField(default=True)

class ContadorDeCurriculum(models.Model):
    contadorCurriculum = models.IntegerField(default=0)
