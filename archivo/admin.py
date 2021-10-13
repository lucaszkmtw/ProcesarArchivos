from django.contrib import admin

from archivo.models import ArchivoHiscar


# Register your models here.



@admin.register(ArchivoHiscar)
class ArchivoHiscarAdmin(admin.ModelAdmin):
    model = ArchivoHiscar
    list_filter = ('autor','fileHash')
    actions = [
        'parse_file'
    ]

            