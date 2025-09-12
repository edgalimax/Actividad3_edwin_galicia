from django.contrib import admin
from .models import Estudiante, Curso, Telefono, Publicacion

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Telefono)
admin.site.register(Publicacion)
