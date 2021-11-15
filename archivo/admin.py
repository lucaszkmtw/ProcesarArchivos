from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.http import HttpResponseRedirect
from archivo.models import ArchivoHiscar, Cargo, CodigoLargo, Reparticion, Hiscar
from django.shortcuts import render
from django.utils.html import format_html
# Register your models here.
from archivo.tasks import procesar, task
import os
from archivo import tasks
from django.http import JsonResponse

class ArchivoHiscarAdmin(admin.ModelAdmin):
    model = ArchivoHiscar
    list_filter = ('autor', 'fileHash')
    list_display = ('__str__', 'parsed', 'procesado')
    actions = [
        'parse_file'
    ]

    class Media:
        js = [
            'js/home.js',
            'celery_progress/celery_progress.js',
            'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'
        ]

    def parse_file(self, request, queryset):
            for archivo in queryset:

                queryset.update(parsed=True)

            self.message_user(request,
                              "archivos procesados, se han obtenido {} hiscar ".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())

    parse_file.short_description = "Process %(verbose_name_plural)s seleccionados/as"


admin.site.register(CodigoLargo)
admin.site.register(ArchivoHiscar, ArchivoHiscarAdmin)
admin.site.register(Reparticion)
admin.site.register(Cargo)
admin.site.register(Hiscar)
