from django.contrib import admin
from .models import Perro, Adopcion, Adoptante

# Register your models here.

admin.site.register(Perro)

admin.site.register(Adoptante)

admin.site.register(Adopcion)
