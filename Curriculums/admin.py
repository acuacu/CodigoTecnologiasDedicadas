from django.contrib import admin
from .models import Curriculum, Flyers, PaginasWeb, DatosUsuario, ContadorDeCurriculum
# Register your models here.
@admin.register(Curriculum)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'Email', 'Pais', 'CuentaPaga')
@admin.register(Flyers)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'link')
@admin.register(PaginasWeb)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'link')
@admin.register(DatosUsuario)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'NumeroDeTelefono', 'DeQueTrabajo', 'SegundoFactorDeAutentificacion')
@admin.register(ContadorDeCurriculum)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('contadorCurriculum', 'pk')
