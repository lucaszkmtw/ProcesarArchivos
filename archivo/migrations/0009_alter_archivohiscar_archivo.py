# Generated by Django 3.2.7 on 2021-11-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivo', '0008_cargo_hiscar_reparticion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivohiscar',
            name='archivo',
            field=models.FilePathField(null=True, path='uploads/'),
        ),
    ]
