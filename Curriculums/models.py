
from django.db import models
from django.contrib.auth.models import User
import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from .validators import valid_extension

def generate_path(instance, filename):
    usuario = str(instance.CuentaDelUsuario)
    filename = 'FotoDePortada_' + str(instance.CuentaDelUsuario) + '.jpg'
    basedirr = os.path.join('static/media/'+ usuario +'/FotoDePortada/', filename)
    basedir = os.path.join('static/media/'+ usuario +'/FotoDePortada/')
    if not os.path.exists(basedir):
        os.makedirs(basedir)
        with open(basedirr, 'a'):
            os.utime(basedirr, None)

    ttt = os.remove(os.path.join('static/media/'+ usuario +'/FotoDePortada/', filename))
    return os.path.join(usuario +'/FotoDePortada/', filename)

def generate_path_avatar(instance, filename):
    usuario = str(instance.CuentaDelUsuario)
    filename = 'FotoDePerfil_' + str(instance.CuentaDelUsuario) + '.jpg'
    basedirr = os.path.join('static/media/'+ usuario +'/FotoDePerfil/', filename)
    basedir = os.path.join('static/media/'+ usuario +'/FotoDePerfil/')
    if not os.path.exists(basedir):
        os.makedirs(basedir)
        with open(basedirr, 'a'):
            os.utime(basedirr, None)

    ttt = os.remove(os.path.join('static/media/'+ usuario +'/FotoDePerfil/', filename))
    return os.path.join(usuario +'/FotoDePerfil/', filename)


class DatosUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.OneToOneField(User, on_delete=models.CASCADE)
    NumeroDeTelefono = models.CharField(max_length=256, default='Mi número...')
    DeQueTrabajo = models.CharField(max_length=256, default='Traba de..')
    SegundoFactorDeAutentificacion = models.BooleanField(default=True)
    UsuarioDestacado = models.BooleanField(default=False)

class FotoDePerfil(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.OneToOneField(User, on_delete=models.CASCADE)
    FotoDePerfil = models.ImageField(upload_to=generate_path_avatar, null=True, blank=True)
class FotoDelPortada(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.OneToOneField(User, on_delete=models.CASCADE)
    FotoDePortada = models.ImageField(upload_to=generate_path, null=True, blank=True)













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
    UsuarioDestacados = models.BooleanField(default=False)
    pkUsuario = models.IntegerField(default=0)

def generate_path_flyer(instance, filename):
    usuario = str(instance.CuentaDelUsuario)

    return os.path.join(usuario +'/flyers/', filename)


class Flyers(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, default='www.tecnologiasdedicadas.com/Curriculum/{{ user.pk }}')
    flyers = models.ImageField(upload_to=generate_path_flyer, null=True, blank=True)


def generate_path_diploma(instance, filename):
    usuario = str(instance.CuentaDelUsuario)

    return os.path.join(usuario +'/diplomas/', filename)


class Diplomas(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, default='www.tecnologiasdedicadas.com/Curriculum/{{ user.pk }}')
    diploma = models.ImageField(upload_to=generate_path_diploma, null=True, blank=True)




class PaginasWeb(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, default='Agregar una Web')


class ContadorDeCurriculum(models.Model):
    contadorCurriculum = models.IntegerField(default=0)
