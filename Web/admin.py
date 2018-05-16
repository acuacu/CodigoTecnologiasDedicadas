from django.contrib import admin
from .models import Ticket, Comentario
# Register your models here.

@admin.register(Ticket)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'Asunto', 'Mensaje', 'Remitente')


@admin.register(Comentario)
class AdminCVMasComentario(admin.ModelAdmin):
    list_display = ('text_usuarios_comentarios', 'text_usuarios_comentarios', 'text_del_comentario')
