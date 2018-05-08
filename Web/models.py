from django.db import models
from django.contrib.auth.models import User
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    CuentaDelUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Asunto = models.CharField(max_length=256, default='Asunto')
    Mensaje = models.CharField(max_length=256, default='Mensaje')
    Remitente = models.CharField(max_length=256)
    FechaDeCreacion = models.DateTimeField(auto_now_add=True)
    Respondido = models.BooleanField(default=False)
    mostrar = models.BooleanField(default=True)

class Contacto(models.Model):
    text_usuario_contacto = models.CharField(max_length=256)
    text_email_contacto = models.EmailField(max_length=254)
    text_asunto_contacto = models.CharField(max_length=256)
    text_texo_del_contacto = models.CharField(max_length=256)
    fecha_de_comentario = models.DateTimeField(auto_now_add=True)
    link_imagen = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.text_usuario_contacto
    class Meta:
        ordering = ('id',)


class Comentario(models.Model):
    text_usuarios_comentarios = models.CharField(max_length=1000)
    text_del_comentario = models.CharField(max_length=1000)
    fecha_de_comentario = models.DateTimeField(auto_now_add=True)
    link_imagen_izquierda = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.text_usuarios_comentarios
    class Meta:
        ordering = ('id',)
