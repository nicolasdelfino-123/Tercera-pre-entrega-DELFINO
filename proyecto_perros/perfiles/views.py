from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Avatar

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario

###### VIEW DE REGISTRO ###########################
def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('index') #aca decia inicio y puse 'index'
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

####### VIEW DE LOGIN #################################

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)
       form.fields['username'].label = 'Usuario' 
       form.fields['password'].label = 'Contraseña'
       
       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('index')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
       form.fields['username'].label = 'Usuario'
       form.fields['password'].label = 'Contraseña' 
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
    )
   
   
   ####logout view basada en clase#######################
   
class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'
   
   ####ESTE CODIGO ES PARA QUE ME MUESTRE CHAU NOMBRE_USUARIO EN LOGOUT.HTML, NO FUNCIONA
#    def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context['nombre_usuario'] = self.request.user.username
#         return context
   

#Agrega esto al final del archivo
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('index')
   template_name = 'perfiles/formulario_perfil.html'

   def get_object(self, queryset=None):
       return self.request.user
   
   
#viejo formulario avatar
# @login_required
# def agregar_avatar(request):
#     if request.method == "POST":
#         formulario = AvatarFormulario(request.POST, request.FILES)

#         if formulario.is_valid():
#             avatar = formulario.save(commit=False)
#             avatar.user = request.user
#             avatar.save()
#             url_exitosa = reverse('index')
#             return redirect(url_exitosa)
#     else:  # GET
#         formulario = AvatarFormulario()

#     # Obtener el avatar del usuario actual
#     avatar_usuario = Avatar.objects.get(user=request.user) if Avatar.objects.filter(user=request.user).exists() else None

#     return render(
#         request=request,
#         template_name="perfiles/formulario_avatar.html",
#         context={'form': formulario, 'avatar': avatar_usuario}
#     )

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar_anterior = Avatar.objects.filter(user=request.user)
            if (len(avatar_anterior) > 0):
                avatar_anterior.delete()
            avatar_nuevo = Avatar(user=request.user, imagen=formulario.cleaned_data["imagen"])
            avatar_nuevo.save()
            url_exitosa = reverse('index')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()

    # Obtener el avatar del usuario actual
    avatar_usuario = Avatar.objects.get(user=request.user) if Avatar.objects.filter(user=request.user).exists() else None

    return render(
        request=request,
        template_name="perfiles/formulario_avatar.html",
        context={'form': formulario, 'avatar': avatar_usuario}
    )