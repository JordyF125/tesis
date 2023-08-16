# Generated by Django 4.2.4 on 2023-08-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0021_alter_deportista_clave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deportista',
            name='clave',
            field=models.CharField(max_length=100, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='deportista',
            name='usuario',
            field=models.CharField(max_length=100, unique=True, verbose_name='Usuario'),
        ),
    ]
