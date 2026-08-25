from django.contrib import admin
from .models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    # Para que en el panel se vean estas columnas
    list_display = ('numero_identidad', 'nombre', 'telefono')
    # Para agregar un buscador en el panel de admin
    search_fields = ('numero_identidad', 'nombre')

admin.site.register(Paciente, PacienteAdmin)