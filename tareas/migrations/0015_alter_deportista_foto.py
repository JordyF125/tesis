# Generated by Django 4.2.4 on 2023-08-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0014_alter_deportista_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deportista',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/tareas/images/'),
        ),
    ]
