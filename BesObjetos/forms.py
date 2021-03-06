from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, CharField, PasswordInput
from django.contrib.auth.models import User




class UserRegister(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Repetir Contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Repetir Contraseña", widget=PasswordInput)

    class Meta: 
        model = User
        fields = ["email", "password1", "password2"]
        help_text = {k:"" for k in fields}