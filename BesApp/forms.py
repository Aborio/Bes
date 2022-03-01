from django import forms
from django.forms import Form

class PersonaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()

class ComprasFormulario(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()

class AvatarFormulario(Form):
    imagen = forms.ImageField(required=True)


