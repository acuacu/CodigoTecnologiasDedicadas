from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ClearableFileInput
from .models import Curriculum, DatosUsuario,FotoDePerfil, FotoDelPortada

class DatosPersonales(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ('Nombre', 'Direccion', 'Pais', 'Nacimiento', 'Edad', 'Dni', 'Email', 'Telefono')


class FotoDePerfilFormulario(forms.ModelForm):
    class Meta:
        model = FotoDePerfil
        fields = ('FotoDePerfil',)


class FotoDelPortadaFormulario(forms.ModelForm):
    class Meta:
        model = FotoDelPortada
        fields = ('FotoDePortada',)
