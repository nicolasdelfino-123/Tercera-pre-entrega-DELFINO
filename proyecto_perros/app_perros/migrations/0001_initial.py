# Generated by Django 4.2.1 on 2023-05-20 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('tamanio', models.CharField(max_length=20)),
                ('fecha_entrada', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perros/')),
                ('edad', models.CharField(max_length=10)),
                ('raza', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('descripcion', models.TextField(blank=True)),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_adopcion', models.DateTimeField(auto_now=True)),
                ('adoptante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_perros.adoptante')),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('perro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_perros.perro')),
            ],
        ),
    ]
