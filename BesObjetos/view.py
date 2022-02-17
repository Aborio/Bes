from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from BesApp.forms import AvatarFormulario
from BesApp.models import Avatar
from BesObjetos.forms import UserRegister, UserEditForm, User
from BesObjetos.view import UserCreationForm
from django.contrib.auth.decorators import login_required



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]  
            contrasena = form.cleaned_data["password"]
            user = authenticate(username=usuario, password= contrasena)
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, "BesApp/login.html", {"form" : form, "error" : "No es valido el usuario y la constraseña"})
        else:
            return render(request, "BesApp/login.html", {"form" : form})  
    else:    
        form = AuthenticationForm()
        return render(request, "BesApp/login.html", {"form" : form})


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return HttpResponse(f"Usuario {username} creado correctamente")
    else:
        form = UserRegister()
    return render(request, "BesApp/register.html", {'form' : form})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data ['email']
            usuario.password1 = data ['password1']
            usuario.password2 = data ['password2']
            usuario.save()
            return redirect("inicio")
    else:
        formulario = UserEditForm({'email' : usuario.email})
    return render (request, 'BesApp/register.html' , {'form' : formulario})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.files)
        if miFormulario.is_valid:
            u = User.objects.get(username=request.user)
            avatar = Avatar (user=u, imagen= miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render (request, 'BesApp/inicio.html')
    else:
        miFormulario = AvatarFormulario()        
    return render (request, "BesApp/agregarAvatar.html", {"miFormulario": miFormulario})


def error404(request, exception):
    return render (request, "BesApp/404error.html")

