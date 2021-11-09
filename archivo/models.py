from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.files import File
import os
# Create your models here.


class Reparticion(models.Model):
    codigo = models.CharField(max_length=6, db_index=True)
    nombre = models.CharField(max_length=500, db_index=True)
    has_modulo = models.BooleanField(default=False)

    class Meta:
        db_table = 'reparticiones'

    def __str__(self):
        return self.codigo + ' - ' + self.nombre


class Cargo(models.Model):
    reparticion = models.ForeignKey(
        Reparticion,
        default=None,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="Cargo_reparticion")
    codigo = models.CharField(max_length=15, db_index=True)
    cargo = models.CharField(max_length=200, db_index=True)


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
    archivo = models.FilePathField(
        path='uploads/', allow_files=True, null=True)
    fecha = models.DateTimeField(default=now)
    parsed = models.BooleanField(default=False, null=True)

    def __str__(self):
        if self.archivo:

            nombre = str(self.archivo.split('/')[-1])
            peso = float(os.path.getsize(self.archivo)) / 1024
            peso  = str(peso)[0:4]
            return f'{nombre}'
        else:
            return '-'


class CodigoLargo(models.Model):
    codigo = models.CharField(max_length=550, blank=True, null=True)
    created = models.DateTimeField(default=now)

    def __str__(self):
        return f'{str(self.id)} - {self.codigo} '


class Hiscar(models.Model):
    periodo = models.DateField(
        auto_now=False,
        auto_now_add=False,
        default=None,
        null=True,
        db_index=True)
    cargo = models.CharField(max_length=11, db_index=True)
    reparticion = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        default=None,
        db_index=True)
    basico = models.DecimalField(
        max_digits=18,
        decimal_places=2)
    suplemento1 = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True)
    suplemento2 = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True)
    antiguedad = models.TextField(
        null=True,
        default=None)
    sumafija1 = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True)
    sumafija2 = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True)
    sumafija3 = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True)
    cargo_obj = models.ForeignKey(
        Cargo,
        default=None,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="cargo_objecto")
    reparticion_obj = models.ForeignKey(
        Reparticion,
        default=None,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="Reparticion_objecto")

    HLS = {
        'periodo': {'dd': 1, 'ht': 8},
        'reparticion': {'dd': 10, 'ht': 14},
        'cargo': {'dd': 14, 'ht': 25}}

    HLS2 = {
        'basico': {'dd': 26, 'ht': 38},
        'suplemento1': {'dd': 39, 'ht': 51},
        'suplemento2': {'dd': 52, 'ht': 64},
        'antiguedad': {'dd': 65, 'ht': 77},
        'sumafija1': {'dd': 78, 'ht': 90},
        'sumafija2': {'dd': 91, 'ht': 104},
        'sumafija3': {'dd': 105, 'ht': 118}}

    HLSV = {
        'periodo': {'dd': 0, 'ht': 6},
        'reparticion': {'dd': 6, 'ht': 10},
        'cargo': {'dd': 10, 'ht': 21}}

    HLSV2 = {
        'basico': {'dd': 21, 'ht': 32},
        'suplemento1': {'dd': 32, 'ht': 43},
        'suplemento2': {'dd': 43, 'ht': 54},
        'antiguedad': {'dd': 54, 'ht': 505},
        'sumafija1': {'dd': 505, 'ht': 516},
        'sumafija2': {'dd': 516, 'ht': 527},
        'sumafija3': {'dd': 527, 'ht': 536}}

    class Meta:
        db_table = 'hiscars'
        unique_together = [['periodo', 'cargo', 'reparticion']]

    def __str__(self):
        """__str__ Hiscar to string.

        Returns:
            string : formato de impresion de Hiscar.
        """
        return str(self.periodo) + ' - ' + self.cargo
