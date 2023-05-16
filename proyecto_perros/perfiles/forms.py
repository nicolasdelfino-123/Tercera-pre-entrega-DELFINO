from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
       
######FORMULARIO DE LOGIN########
