from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.http import HttpResponseRedirect
from archivo.models import ArchivoHiscar, CodigoLargo
from django.shortcuts import render

# Register your models here.


@admin.register(ArchivoHiscar)
class ArchivoHiscarAdmin(admin.ModelAdmin):
    model = ArchivoHiscar
    list_filter = ('autor', 'fileHash')
    actions = [
        'parse_file' 
    ]

    def parse_file(self, request, queryset):
        if 'apply' in request.POST:
            for archivo in queryset:
                file1 = open("media/{archivo}".format(), 'r')

                for line in file1:
                    linea = "{}".format(line.strip())
                    CodigoLargo.codigo = linea
                    CodigoLargo.save()

            # Closing files
                file1.close()
                queryset.update(parsed=True)
            self.message_user(request,
                              "se han procesado {} archivos".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())

        return render(request, 'admin/procesar.html', {'orders': queryset})


   


admin.site.register(CodigoLargo)
