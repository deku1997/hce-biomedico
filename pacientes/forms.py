from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # Campos que aparecerán en el formulario
        fields = ['numero_identidad', 'nombre', 'fecha_nacimiento', 'telefono', 'direccion', 'foto']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),  # Calendario
        }
        labels = {
            'foto': 'Adjuntar Foto o Documento (Opcional)',
        }