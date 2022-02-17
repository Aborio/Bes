from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()

class ComprasFormulario(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)


