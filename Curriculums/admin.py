from django.contrib import admin
from .models import Curriculum, Flyers, PaginasWeb, DatosUsuario, ContadorDeCurriculum, Diplomas
# Register your models here.
@admin.register(Curriculum)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'Email', 'Pais', 'CuentaPaga','UsuarioDestacados', 'pkUsuario')
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
@admin.register(Diplomas)
class AdminCVMasDatosdelUsuario(admin.ModelAdmin):
    list_display = ('CuentaDelUsuario', 'pk')
