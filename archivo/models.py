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
    archivo = models.FilePathField(path='media/', allow_files=True, null=True)
    fecha = models.DateTimeField(default=now)
    parsed = models.BooleanField(default=False, null=True)
    def __str__(self):
        if self.archivo:
            return str(self.archivo.split('/')[-1])
        else:
            return '-'


class CodigoLargo(models.Model):
    codigo = models.CharField(max_length=550, blank=True, null=True)
    created    = models.DateTimeField(default=now)

