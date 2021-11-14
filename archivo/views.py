from django.shortcuts import render
from .tasks import task
from celery import shared_task
# Create your views here.
import os



def index(request):

    peso = os.path.getsize('uploads/myfile.txt')/537
    tarea= task.delay(int(peso))
    context = {
        'tarea':tarea,
        'task':tarea.task_id,
        'peso':peso
    }
    return render(request, 'archivo/home.html' , context)