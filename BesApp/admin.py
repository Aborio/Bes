from django.contrib import admin
from BesApp.models import Avatar

from BesApp.models import Compras, Persona, Productos
from BesApp.views import persona_delete

# Register your models here.
admin.site.register(Persona)
admin.site.register(Compras)
admin.site.register(Productos)
admin.site.register(Avatar)