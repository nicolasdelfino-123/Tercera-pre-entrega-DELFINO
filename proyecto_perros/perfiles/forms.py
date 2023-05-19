from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from perfiles.models import Avatar
####FORMULARIO DE REGISTRO#####

class UserRegisterForm(UserCreationForm):
   # Esto es un ModelForm
   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
   first_name = forms.CharField(label='Nombre')
   last_name = forms.CharField(label='Apellido')
   username = forms.CharField(label='Nombre de usuario')
   email = forms.EmailField(label='Email')

   class Meta:
       model = User
       fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
       
###haciendo avatar
class UserUpdateForm(forms.ModelForm):

   class Meta:
       model = User
       fields = ['last_name', 'first_name', 'email']
       labels = { 'last_name':'Apellido',
                 'first_name': 'Nombre',
                 'email': 'Correo electrónico'
                
        }


# Agregar al final del archivo
class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']