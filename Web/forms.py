from django import forms
from .models import Contacto, Comentario
from django.contrib.auth.models import User
from django.forms import ModelForm, ClearableFileInput


class AgregarContactosWeb(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class AgregarComentariosWeb(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
