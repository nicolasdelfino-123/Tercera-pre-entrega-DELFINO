# Generated by Django 4.2.1 on 2023-05-08 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_perros', '0003_remove_adopcion_nombre_remove_adoptante_perro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='perro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_perros.perro'),
        ),
    ]