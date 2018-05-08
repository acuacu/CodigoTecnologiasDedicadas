from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ClearableFileInput
from .models import Curriculum


class DatosPersonales(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ('Nombre', 'Direccion', 'Pais', 'Nacimiento', 'Edad', 'Dni', 'Email', 'Telefono')
