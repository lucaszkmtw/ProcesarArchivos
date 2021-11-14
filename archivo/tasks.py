import os
import shutil
import resource
from django.conf import settings
from celery_progress.backend import ProgressRecorder
from ProcesarArchivos.celery import app

@app.task(bind=True)
def task(self, duration):
    progreso =  ProgressRecorder(self)
    file1 = open('uploads/myfile.txt', 'r')
    count = 0
    lista = []

    for line in file1:
        linea = "{}".format(line.strip())
        lista.append(linea)
        count = count + 1
        progreso.set_progress(count + 1 , duration, f'va por {count}')
    # Closing files
    file1.close()
