# Generated by Django 4.2.4 on 2023-08-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0006_alter_rendimientoinscripcion_posicion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendimientoinscripcion',
            name='tiempominutos',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rendimientoinscripcion',
            name='tiemposegundos',
            field=models.FloatField(),
        ),
    ]