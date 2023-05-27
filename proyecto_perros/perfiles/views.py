from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import UserUpdateForm, CustomPasswordChangeForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario


def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  
           url_exitosa = reverse('index') 
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )


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
   
   
class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'
   

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'perfiles/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'password_formulario' not in context:
            context['password_formulario'] = CustomPasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        password_formulario = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid() and password_formulario.is_valid():
            return self.form_valid(form, password_formulario)
        else:
            return self.form_invalid(form, password_formulario)

    def form_valid(self, form, password_formulario):
        self.object = form.save(commit=False)
        self.object.save()

        if password_formulario.is_valid():
            user = password_formulario.save()
            update_session_auth_hash(self.request, user)
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form, password_formulario=password_formulario))

    def form_invalid(self, form, password_formulario):
        return self.render_to_response(self.get_context_data(form=form, password_formulario=password_formulario))


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
    
   
    
    