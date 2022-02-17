from django.urls import path
from BesObjetos.view import agregarAvatar
from BesApp.views import About, persona_update
from BesApp.views import persona_delete, compra_delete, producto_delete
from BesApp.views import buscar, busquedaDatos
from BesApp.views import padre
from BesApp.views import Personas
from BesApp.views import personaFormulario, productoFormulario, comprasFormulario
from BesApp import views
from django.urls import path
from BesApp.views import inicio, Producto, Compra

urlpatterns = [
    path("", padre, name = "padre"),
    path("personaFormulario/", personaFormulario, name = "Perform"),
    path("personas/", Personas, name = "personas"),
    path("inicio/", inicio, name = "inicio"),
    path("productos/", Producto, name = "productos"),
    path("productoFormulario/", productoFormulario , name = "Proform"),
    path("compras/", Compra , name = "compras"),
    path("comprasFormulario/", comprasFormulario , name = "Comform" ),
    path("busquedaDatos/", busquedaDatos, name ="busquedaDat"),
    path("buscar/", buscar),
    path("persona/delete/<id_persona>", persona_delete, name="persdelete"),
    path("producto/delete/<id_productos>", producto_delete, name="prodelete"),
    path("compra/delete/<id_compra>", compra_delete, name="comdelete"),
    path("persona/update/<id_persona>", persona_update, name = "Pupdate"),
    path("about", About, name = "abouT"),
    path("agregarAvatar", agregarAvatar, name = "agregarAvatar")



]   
