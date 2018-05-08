from django.contrib import admin
from .models import Ticket
# Register your models here.

@admin.register(Ticket)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'Asunto', 'Mensaje', 'Remitente')
