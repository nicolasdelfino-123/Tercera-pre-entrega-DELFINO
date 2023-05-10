from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Perro

from app_perros.forms import AdoptanteFormulario, AdopcionFormulario, PerroFormulario, BuscarPerro
from app_perros.models import Perro
from app_perros.models import Adoptante
from app_perros.models import Adopcion



# vista de busqueda ########################################################################
def buscar_perro(request):
    if request.method == "POST":
        formulario = BuscarPerro(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            tamanio = data['tamanio']
            perros = Perro.objects.filter(tamanio__icontains=tamanio)
            # perros = Perro.objects.all()
            contexto = {
                "perros": perros,
            }
            http_response = render(
            request=request,
            template_name='app_perros/lista_perros.html',
            context=contexto,
        )
        return http_response
    
    else:  # GET
        formulario = BuscarPerro()
        http_response = render(
            request=request,
            template_name='app_perros/buscar_perros.html',
            context={'formulario': formulario}
        )
        return http_response

# def search(request):
#     form = SearchForm()
#     results = None
#     if request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             search_term = form.cleaned_data['search_term']
#             # Realiza la búsqueda en la base de datos utilizando el término de búsqueda
#             results = Perro.objects.filter(nombre__icontains=search_term)
#     return render(request, 'app_perros/search.html', {'form': form, 'results': results})

# Vistas de Perro ##########################################################################

def crear_perro(request):
    '''vista para crear perro'''
    if request.method == "POST":
        formulario = PerroFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            tamanio = data['tamanio']
            fecha_entrada = data['fecha_entrada']
            perro = Perro(nombre=nombre, tamanio=tamanio, fecha_entrada=fecha_entrada)
            perro.save()
        
            # Redireccionar al usuario a la lista de perros
            url_exitosa = reverse('listar_perros')
            return redirect(url_exitosa)
            

    else:  # GET
        formulario = PerroFormulario()

    http_response = render(
        request=request,
        template_name='app_perros/formulario_perro.html',
        context={'formulario': formulario}
    )
    return http_response


def listar_perros(request):
    '''vista para listar perrros'''
    contexto = {
        "perros": Perro.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_perros/lista_perros.html',
        context=contexto,
    )
    return http_response


# Vistas de Adoptante ##########################################################################

def crear_adoptante(request):
    '''vista para crear adoptantes'''
    if request.method == "POST":
        formulario = AdoptanteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            apellido = data ['apellido']
            nombre = data ['nombre']
            email = data ['email']
            telefono = data ['telefono']
            dni = data ['dni']
            fecha_nacimiento = data ['fecha_nacimiento']
            adoptante = Adoptante(nombre=nombre,apellido=apellido,email=email,telefono=telefono,dni=dni,fecha_nacimiento=fecha_nacimiento )
            adoptante.save()
            
            
            # Redirecciono al usuario a la lista de perros
            url_exitosa = reverse('listar_adoptante')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = AdoptanteFormulario()
    http_response = render(
        request=request,
        template_name='app_perros/formulario_adoptante.html',
        context={'formulario': formulario}
    )
    return http_response

def listar_adoptantes(request):
    '''vista para listar adoptantes'''
    contexto = {
        "adoptantes": Adoptante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_perros/lista_adoptante.html',
        context=contexto,
    )
    return http_response
    
    ######### vistas de adopcion
    
def crear_adopcion(request):
    '''vista para crear adopcion'''
    if request.method == "POST":
        formulario = AdopcionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            adoptante = data['adoptante']
            perro = data['perro']
            adopcion = Adopcion(adoptante=adoptante, perro=perro)
            adopcion.save()
    
            # Redirecciono al usuario a la lista de adopciones
            url_exitosa = reverse('listar_adopcion')  
            return redirect(url_exitosa)

    else:  # GET
        formulario = AdopcionFormulario()

    http_response = render(
        request=request,
        template_name='app_perros/formulario_adopcion.html',
        context={'formulario': formulario}
    )
    return http_response

def listar_adopcion(request):
    '''vista para listar adopcion'''
    contexto = {
        "adopciones": Adopcion.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_perros/lista_adopcion.html',
        context=contexto,
    )
    return http_response    