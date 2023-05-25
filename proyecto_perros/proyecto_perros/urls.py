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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_perros.views import listar_perros, crear_adoptante, listar_adoptantes, crear_adopcion,\
    listar_adopcion, crear_perro, buscar_perro, eliminar_perro, editar_perro, about, ver_mas,\
    eliminar_adoptante, felicitaciones_adopcion, mensaje_error, mensaje_error2,error_creacion_adoptante

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", listar_perros, name="index"),
    path("crear_perro/", crear_perro, name="crear_perro"),
    path("perros/", listar_perros, name="listar_perros"),
    path("crear_adoptante/", crear_adoptante, name="crear_adoptante"),
    path("listar_adopcion/", listar_adopcion, name="listar_adopcion"),
    path("listar_adoptante/", listar_adoptantes, name="listar_adoptante"),
    path("crear_adopcion/", crear_adopcion, name="crear_adopcion"),
    path('error/', mensaje_error, name='error_adopcion'),
    path('error-2/', mensaje_error2, name='error_adopcion2'),
    path('error_creacion_adoptante/', error_creacion_adoptante, name='error_creacion_adoptante'),
    path('buscar_perros/', buscar_perro, name='buscar_perros'),
    path('felicitaciones-adopcion/<str:nombre_perro>/', felicitaciones_adopcion, name='felicitaciones_adopcion'),
    path('eliminar-adoptante/<int:adoptante_id>/', eliminar_adoptante, name='eliminar_adoptante'), 
    path('eliminar-perro/<int:perro_id>/', eliminar_perro, name="eliminar_perro"),#DELETE
    path('editar-perro/<int:id>/', editar_perro, name="editar_perro"),
    path('ver-mas/<int:perro_id>/', ver_mas, name='ver_mas'),
    path("perfiles/", include('perfiles.urls')),
    path("about/", about , name='about')
     
    #####
    # path('adoptante/', AdoptanteListView.as_view(), name='listar_adoptante'),
    # path('adoptantes/<int:pk>/', AdoptanteDetailView.as_view(), name="ver_adoptante"),##
    # path('crear-adoptante/', AdoptanteCreateView.as_view(), name="crear_adoptante"),
    # path('editar-adoptante/<int:pk>/', AdoptanteUpdateView.as_view(), name="editar_adoptante"),###
    # path('eliminar-adoptante/<int:pk>/', AdoptanteDeleteView.as_view(), name="eliminar_adoptante"),##
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
