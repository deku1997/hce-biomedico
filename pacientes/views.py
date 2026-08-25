from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

# 1. PÁGINA DE INICIO
def inicio(request):
    return render(request, 'inicio.html')

# 2. REGISTRAR PACIENTE
def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'registrar_paciente.html', {'form': form})

# 3. LISTA DE PACIENTES
def lista_pacientes(request):
    pacientes = Paciente.objects.all().order_by('-id')
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

# 4. BUSCADOR POR IDENTIDAD
def buscar_paciente(request):
    identidad = request.GET.get('identidad', '')
    paciente = None
    error = None
    if identidad:
        try:
            paciente = Paciente.objects.get(numero_identidad=identidad)
        except Paciente.DoesNotExist:
            error = f"No se encontró ningún paciente con identidad: {identidad}"
    return render(request, 'buscar_paciente.html', {
        'paciente': paciente,
        'error': error,
        'identidad': identidad
    })