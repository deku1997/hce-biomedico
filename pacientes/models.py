from django.db import models

class Paciente(models.Model):
    numero_identidad = models.CharField(max_length=20, unique=True, verbose_name="N° Identidad")
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    direccion = models.TextField(blank=True, null=True, verbose_name="Dirección")
    
    # 🔥 Campo para subir imágenes/documentos
    foto = models.ImageField(
        upload_to='pacientes/fotos/',
        blank=True,
        null=True,
        verbose_name="Foto / Documento adjunto"
    )

    def __str__(self):
        return f"{self.nombre} - {self.numero_identidad}"