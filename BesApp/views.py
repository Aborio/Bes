from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from BesApp import admin
from BesApp.forms import PersonaFormulario, ProductoFormulario, ComprasFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from BesApp.models import Persona, Productos, Compras
from BesApp.models import Avatar

# Create your views here.

def padre(request):
    return render(request,'BesApp/padre.html')

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request,'BesApp/inicio.html', {'avatar_url' : avatar_url})

def Personas(request):
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render (request, 'BesApp/personas.html', {"personas" : Persona.objects.all,'avatar_url' : avatar_url})

def Producto(request):
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render (request, 'BesApp/productos.html', {"productos" : Productos.objects.all, 'avatar_url' : avatar_url})

def Compra(request):
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render (request, 'BesApp/compras.html', {"compras": Compras.objects.all, 'avatar_url' : avatar_url})

def personaFormulario(request):
    if request.method == "POST":
        formulario = PersonaFormulario(request.POST)

        
        if formulario.is_valid():

            data = formulario.cleaned_data

            Persona.objects.create(nombre = data['nombre'], apellido = data['apellido']) 

            return redirect("personas")
    else:
    
        formulario = PersonaFormulario()
    return render(request, 'BesApp/personaFormulario.html', {"formulario": formulario})

def productoFormulario(request):
    if request.method == "POST":
        Pformulario = ProductoFormulario(request.POST)

        
        if Pformulario.is_valid():

            Pdata = Pformulario.cleaned_data

            Productos.objects.create(nombre= Pdata['nombre'], tipo= Pdata['tipo'])

            return redirect("productos")
    else:
    
        Pformulario = ProductoFormulario()
    return render(request, 'BesApp/productoFormulario.html', {"Pformulario": Pformulario})

def personaFormulario(request):
    if request.method == "POST":
        formulario = PersonaFormulario(request.POST)

        
        if formulario.is_valid():

            data = formulario.cleaned_data

            Persona.objects.create(nombre = data['nombre'], apellido = data['apellido']) 

            return redirect("personas")
    else:
    
        formulario = PersonaFormulario()
    return render(request, 'BesApp/personaFormulario.html', {"formulario": formulario})

def comprasFormulario(request):
    if request.method == "POST":
        Cformulario = ComprasFormulario(request.POST)

        
        if Cformulario.is_valid():

            Cdata = Cformulario.cleaned_data

            Compras.objects.create(nombre= Cdata['nombre'], tipo= Cdata['tipo'])

            return redirect("compras")
    else:
    
        Cformulario = ComprasFormulario()
    return render(request, 'BesApp/comprasFormulario.html', {"Cformulario": Cformulario})
def busquedaDatos (request):

    return render (request, "BesApp/busquedaDatos.html")

def buscar(request):
    #respuesta = f"Estoy buscando el dato: {request.GET ['nombre']}"
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        personas = Persona.objects.filter(nombre=nombre)
        return render(request, "BesApp/resultadoBusqueda.html", {"nombre": nombre , "personas" : personas})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

@permission_required(perm=[admin])
def persona_delete(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    persona.delete()

    return redirect('personas')

@permission_required(perm=[admin])
def producto_delete(request, id_productos):
    productos = Productos.objects.get(id=id_productos)
    productos.delete()

    return redirect('productos')
@permission_required(perm=[admin])
def compra_delete(request, id_compra):
    compra = Compras.objects.get(id=id_compra)
    compra.delete()

    return redirect('compras')
@permission_required(perm=[admin])
def persona_update(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == "POST":
        formulario = PersonaFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            persona.nombre = data['nombre'],
            persona.apellido = data['apellido'] 

            persona.save()
            return redirect("personas")
    else:
    
        formulario = PersonaFormulario(model_to_dict(persona))
    return render(request, 'BesApp/personaFormulario.html', {"formulario": formulario})

   
def About(request):
    return render (request, 'BesApp/about.html')

