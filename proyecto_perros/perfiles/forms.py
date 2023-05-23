from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from perfiles.models import Avatar
from django.contrib.auth.forms import SetPasswordForm
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
       
##form editar perfil original andando###
# class UserUpdateForm(forms.ModelForm):

#    class Meta:
#        model = User
#        fields = ['last_name', 'first_name', 'email']
#        labels = { 'last_name':'Apellido',
#                  'first_name': 'Nombre',
#                  'email': 'Correo electrónico'
                
#         }

# form mejorado para que actualice password 

class UserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        labels = {
            'last_name': 'Apellido',
            'first_name': 'Nombre',
            'email': 'Correo electrónico'
        }
### esto me hace agregar para mejorar pass



class CustomPasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}),
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar nueva contraseña'}),
    )

##agregado por gpt para limpiar campos adicionales
# class CustomPasswordChangeForm(PasswordChangeForm):
#     def clean(self):
#         cleaned_data = super().clean()
#         return cleaned_data

# Agregar al final del archivo
class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']