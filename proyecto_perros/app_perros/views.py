from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Perro
# from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin # ESTO SE USA EN CLASES EN LOS PARENTESIS(AL PRINCIPIO, LO QUE SIGUE)
from django.contrib.auth.decorators import login_required

from app_perros.forms import AdoptanteFormulario, AdopcionFormulario, PerroFormulario, BuscarPerro
from app_perros.models import Perro
from app_perros.models import Adoptante
from app_perros.models import Adopcion
from django.http import HttpResponseForbidden
from django.contrib import messages


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

# Vistas de Perro original comentada##########################################################################
# @login_required
# def crear_perro(request):
#     '''vista para crear perro'''
#     if request.method == "POST":
#         formulario = PerroFormulario(request.POST, request.FILES)

#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             nombre = data['nombre']
#             tamanio = data['tamanio']
#             fecha_entrada = data['fecha_entrada']
#             foto = data['foto']
#             creador = request.user
#             perro = Perro(nombre=nombre, tamanio=tamanio, fecha_entrada=fecha_entrada, creador=creador, foto=foto)
#             perro.save()

#             # Redireccionar al usuario a la lista de perros
#             url_exitosa = reverse('listar_perros')
#             return redirect(url_exitosa)
#             # return reverse_lazy('listar_perros')

#     else:  # GET
#         formulario = PerroFormulario()

#     context = {'formulario': formulario}
#     http_response = render(
#         request=request,
#         template_name='app_perros/formulario_perro.html',
#         context=context
#     )
#     return http_response

    ####
@login_required
def crear_perro(request):
    if request.method == "POST":
        formulario = PerroFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            tamanio = formulario.cleaned_data['tamanio']
            fecha_entrada = formulario.cleaned_data['fecha_entrada']
            foto = formulario.cleaned_data['foto']
            edad = formulario.cleaned_data['edad']
            raza = formulario.cleaned_data['raza']
            genero = formulario.cleaned_data['genero']
            descripcion = formulario.cleaned_data['descripcion']
            creador = request.user

            perro = Perro(
                nombre=nombre,
                tamanio=tamanio,
                fecha_entrada=fecha_entrada,
                foto=foto,
                edad=edad,
                raza=raza,
                genero=genero,
                descripcion=descripcion,
                creador=creador
            )
            perro.save()

            # Redireccionar al usuario a la lista de perros
            return redirect('listar_perros')

    else:  # GET
        formulario = PerroFormulario()

    context = {'formulario': formulario}
    return render(request, 'app_perros/formulario_perro.html', context)
    ####
def listar_perros(request):
    '''vista para listar perrros'''
    contexto = {
        "perros": Perro.objects.exclude(adopcion__isnull=False),
                   
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
            creador = request.user
            adoptante = Adoptante(nombre=nombre,apellido=apellido,email=email,telefono=telefono,dni=dni,fecha_nacimiento=fecha_nacimiento, creador=creador )
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

##NO LO VOY A USAR PORQUE USARÉ VISTAS BASADAS EN CLASES
@login_required
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
    
def eliminar_adoptante(request, adoptante_id):
    adoptante = get_object_or_404(Adoptante, id=adoptante_id)

    if request.user == adoptante.creador:
        if request.method == 'POST':
            adoptante.delete()
            return redirect('listar_adoptante')
        else:
            return render(request, 'app_perros/eliminar_adoptante.html', {'adoptante': adoptante})
    else:
        return HttpResponseForbidden('No tienes permisos para eliminar este adoptante.')
    
    ######### vistas de adopcion
    


def crear_adopcion(request):
    '''Vista para crear adopcion'''
    if request.method == "POST":
        formulario = AdopcionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            adoptante = data['adoptante']
            perro = data['perro']
            creador = request.user

            # Verificar si el perro ya ha sido adoptado
            if Adopcion.objects.filter(perro_id=perro.id):
                return redirect(reverse('error_adopcion'))
            elif perro.creador == adoptante.creador:
                return redirect(reverse('error_adopcion2'))
            else:
                adopcion = Adopcion(adoptante=adoptante, perro=perro, creador=creador)
                adopcion.save()
                # Redireccionar a la página de felicitaciones
                return redirect(reverse('felicitaciones_adopcion', args=[perro.nombre]))
    else:  # GET
        formulario = AdopcionFormulario()

    context = {
        'formulario': formulario
    }
    return render(request, 'app_perros/formulario_adopcion.html', context)

@login_required
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

# @login_required
# def eliminar_perro(request, id):
#    perro = Perro.objects.get(id=id)
#    if request.method == "POST":
#        perro.delete()
#        url_exitosa = reverse('listar_perros')
#        return redirect(url_exitosa)
   
   #####version 2 de eliminar##################
@login_required
def eliminar_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    
    if request.user == perro.creador:
        if request.method == 'POST':
            perro.delete()
            return redirect('listar_perros')
        else:
            return render(request, 'app_perros/eliminar_perro.html', {'perro': perro})
    else:
        return HttpResponseForbidden('No tienes permisos para eliminar este perro.')
   
   
   
   
@login_required  
def editar_perro(request, id):
   perro = Perro.objects.get(id=id)
   if request.method == "POST":
       formulario = PerroFormulario(request.POST, request.FILES)

       if formulario.is_valid():
           data = formulario.cleaned_data
           perro.nombre = data['nombre']
           perro.tamanio = data['tamanio']
           perro.foto = data ['foto'] if data ['foto'] else perro.foto
           perro.save()
           url_exitosa = reverse('listar_perros')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': perro.nombre,
           'tamanio': perro.tamanio,
           'foto': perro.foto
       }
       formulario = PerroFormulario(initial=inicial)
   return render(
       request=request,
       template_name='app_perros/editar.html',
       context={'formulario': formulario, 'perro': perro},
    )  
   #vista basada en clase de adoptante


#VISTAS BASADAS EN CLASES
# class AdoptanteListView(ListView):
#      model = Adoptante
#      template_name = 'app_perros/lista_adoptante.html'
    
# class AdoptanteCreateView(CreateView):
#      model = Adoptante
#      fields = ('apellido', 'nombre', 'email', 'dni' )
#      success_url = reverse_lazy('listar_adoptante')
    
# class AdoptanteDetailView(DetailView):
#      model = Adoptante
#      success_url = reverse_lazy('listar_adoptante')  
   
# class AdoptanteUpdateView(UpdateView):
#      model = Adoptante
#      fields = ('apellido', 'nombre', 'email', 'dni')
#      success_url = reverse_lazy('listar_adoptante')
     
# class AdoptanteDeleteView(DeleteView):
#      model = Adoptante
#      success_url = reverse_lazy('listar_adoptante')        
         
def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='app_perros/about.html',
        context=contexto,
    )
    return http_response


def ver_mas(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    es_creador = (request.user == perro.creador)
    context = {
        'perro': perro,
        'es_creador': es_creador
    }
    return render(request, 'app_perros/ver_mas.html', context)




def felicitaciones_adopcion(request, nombre_perro):
    return render(request, 'app_perros/felicitaciones_adopcion.html', {'nombre_perro': nombre_perro})


def mensaje_error(request):
    return render (request, 'app_perros/error.html')

def mensaje_error2(request):
    return render (request, 'app_perros/error2.html')