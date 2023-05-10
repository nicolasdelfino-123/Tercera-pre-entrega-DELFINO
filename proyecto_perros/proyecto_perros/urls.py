"""
URL configuration for proyecto_perros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_perros.views import listar_perros, crear_adoptante,listar_adoptantes, crear_adopcion,\
    listar_adopcion, crear_perro, buscar_perro

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", listar_perros, name="index"),
    path("crear_perro/", crear_perro, name="crear_perro"),
    path("perros/", listar_perros, name="listar_perros"),
    path("crear_adoptante/", crear_adoptante, name="crear_adoptante"),
    path("listar_adoptante/", listar_adoptantes, name="listar_adoptante"),
    path("crear_adopcion/", crear_adopcion, name="crear_adopcion"),
    path("listar_adopcion/", listar_adopcion, name="listar_adopcion"),
    path('buscar_perros/', buscar_perro, name='buscar_perros'),


    
    
]
