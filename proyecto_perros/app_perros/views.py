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

# Vistas de Perro ##########################################################################
@login_required
def crear_perro(request):
    '''vista para crear perro'''
    if request.method == "POST":
        formulario = PerroFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            tamanio = data['tamanio']
            fecha_entrada = data['fecha_entrada']
            creador = request.user
            perro = Perro(nombre=nombre, tamanio=tamanio, fecha_entrada=fecha_entrada, creador=creador)
            perro.save()

            # Redireccionar al usuario a la lista de perros
            url_exitosa = reverse('listar_perros')
            return redirect(url_exitosa)
            # return reverse_lazy('listar_perros')

    else:  # GET
        formulario = PerroFormulario()

    context = {'formulario': formulario}
    http_response = render(
        request=request,
        template_name='app_perros/formulario_perro.html',
        context=context
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
       formulario = PerroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           perro.nombre = data['nombre']
           perro.tamanio = data['tamanio']
           perro.save()
           url_exitosa = reverse('listar_perros')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': perro.nombre,
           'tamanio': perro.tamanio,
       }
       formulario = PerroFormulario(initial=inicial)
   return render(
       request=request,
       template_name='app_perros/formulario_perro.html',
       context={'formulario': formulario},
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
    return render(request, 'app_perros/ver_mas.html', {'perro': perro})