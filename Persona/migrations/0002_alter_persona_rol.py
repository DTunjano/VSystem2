# Generated by Django 5.1.1 on 2024-10-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.CharField(choices=[('Estudiante', 'Estudiante'), ('Profesor', 'Profesor')], max_length=50),
        ),
    ]
