from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.http import HttpResponseRedirect
from archivo.models import ArchivoHiscar, Cargo, CodigoLargo, Reparticion, Hiscar
from django.shortcuts import render

# Register your models here.


class ArchivoHiscarAdmin(admin.ModelAdmin):
    model = ArchivoHiscar
    list_filter = ('autor', 'fileHash')
    list_display = ('__str__', 'fecha', 'parsed')
    actions = [
        'parse_file'
    ]

    def parse_file(self, request, queryset):
        for archivo in queryset:
            file1 = open("uploads/{}".format(str(archivo)), 'r')
            count = 0
            for line in file1:
                count += 1
                linea = "{}".format(line.strip())
                codigoNuevo = CodigoLargo(
                    codigo=linea
                )
                codigoNuevo.save()
            # Closing files
            file1.close()

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
