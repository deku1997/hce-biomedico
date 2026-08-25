from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # <-- Ruta principal de la app
    path('registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('lista/', views.lista_pacientes, name='lista_pacientes'),
    path('buscar/', views.buscar_paciente, name='buscar_paciente'),
]