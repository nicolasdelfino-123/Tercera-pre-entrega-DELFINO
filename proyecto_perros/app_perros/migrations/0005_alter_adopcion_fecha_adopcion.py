# Generated by Django 4.2.1 on 2023-05-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_perros', '0004_alter_adopcion_perro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='fecha_adopcion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]