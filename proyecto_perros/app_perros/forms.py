from django import forms
from app_perros.models import Adoptante, Perro

# formulario busqueda #######################################################3

class BuscarPerro(forms.Form):
    tamanio = forms.CharField(label="Tamaño", max_length=100)
    


# from django import forms


# class SearchForm(forms.Form):
#     search_term = forms.CharField(max_length=100)

#################################################################################

class PerroFormulario(forms.Form):
    nombre = forms.CharField(max_length= 64)
    tamanio = forms.CharField(label="Tamaño", max_length=100)
    fecha_entrada= forms.DateField() 


  
class AdoptanteFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256) 
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=32)
    fecha_nacimiento = forms.DateField()
    
    
class AdopcionFormulario(forms.Form):
    adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.all())
    perro = forms.ModelChoiceField(queryset=Perro.objects.all())
    
    
    