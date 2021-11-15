import os
import shutil
import resource
from django.conf import settings
from celery_progress.backend import ProgressRecorder
from ProcesarArchivos.celery import app
from archivo.models import CodigoLargo


@app.task(bind=True)
def task(self, duration):
    progreso = ProgressRecorder(self)
    file1 = open('uploads/myfile.txt', 'r')
    count = 0
    lista = []

    for line in file1:
        linea = "{}".format(line.strip())
        lista.append(linea)
        count = count + 1
        progreso.set_progress(count + 1, duration, f'va por {count}')
    # Closing files
    file1.close()


@app.task(bind=True)
def procesar(self, archivo):
    peso = os.path.getsize(str(archivo))/537
    progreso = ProgressRecorder(self)
    count = 0
    file1 = open(str(archivo), 'r')
    for line in file1:
        count = count + 1
        linea = "{}".format(line.strip())
        codigoNuevo = CodigoLargo(
            codigo=linea
        )
        codigoNuevo.save()
        progreso.set_progress(count, peso, f'va por {count}')
    # Closing files
    file1.close()
