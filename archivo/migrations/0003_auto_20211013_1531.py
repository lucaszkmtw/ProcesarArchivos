# Generated by Django 3.2.8 on 2021-10-13 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivo', '0002_archivohiscar_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivohiscar',
            name='archivo',
        ),
        migrations.RemoveField(
            model_name='archivohiscar',
            name='cant_lineas',
        ),
        migrations.RemoveField(
            model_name='archivohiscar',
            name='parsed',
        ),
        migrations.RemoveField(
            model_name='archivohiscar',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='archivohiscar',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='archivohiscar',
            name='split',
        ),
    ]
