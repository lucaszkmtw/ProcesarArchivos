from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.files import File

# Create your models here.
class ArchivoHiscar(models.Model):
    """
    ArchivoHiscar : modelo que contiene los datos del archivo, del
    cual se importo el "Exporthiscar".

    Args:
        fileHash (char) : Hash para identificar archivo y no repetirlos.
        autor (user) : Usuario que subió el archivo.
        archivo : Nombre del archivo.
        peso (integer) : peso del archivo.
        fecha (date) : fecha de subida del archivo.
    """

    fileHash = models.CharField(
        max_length=33,
        unique=True,
        null=False,
        default='')
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="usuario_cargador")
   
    upload = models.FileField(upload_to='uploads/', null=True)
    fecha = models.DateTimeField(default=now)
  
    def __str__(self):
        return f'{self.fileHash}'.upper()