# Generated by Django 5.1.3 on 2024-12-04 21:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor', '0002_rename__grado_estudianteprimaria_grado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiantesecundaria',
            old_name='especialidad',
            new_name='_especialidad',
        ),
        migrations.AlterField(
            model_name='estudianteprimaria',
            name='grado',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='El grado debe ser al menos 1.'), django.core.validators.MaxValueValidator(6, message='El grado no puede ser mayor que 6.')]),
        ),
    ]
