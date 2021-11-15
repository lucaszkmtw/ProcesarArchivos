from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .tasks import task, procesar
from celery import shared_task
# Create your views here.
import os
from archivo.views import procesar
from django.http import JsonResponse


def index(request):
    # peso = os.path.getsize('uploads/myfile.txt')/537
    # objetos = procesar.delay('uploads/myfile.txt',peso)

    context = {
        #     'peso':peso,
        #     'task':objetos.task_id
    }
    return render(request, 'archivo/home.html', context)


def procesado(request, archivo):
    proceso = procesado.delay(archivo)
    id = proceso.task_id
    context = {
        'ok': 'ok',
        'id': id
    }

    
    return JsonResponse(context)
