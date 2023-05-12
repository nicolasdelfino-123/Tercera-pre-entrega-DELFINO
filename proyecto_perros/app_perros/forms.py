from django import forms
from app_perros.models import Adoptante, Perro

# formulario busqueda 

class BuscarPerro(forms.Form):
     TAMANIO_CHOICES = (
        ('chico', 'Chico'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    )
     tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)
    

class PerroFormulario(forms.Form):
     TAMANIO_CHOICES = (
        ('chico', 'Chico'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
         )
     nombre = forms.CharField(max_length= 64)
     tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)
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
    
    
    