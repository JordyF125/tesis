# Generated by Django 4.2.4 on 2023-08-09 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_rendimientocompetencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='valor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='deportista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.deportista'),
        ),
    ]