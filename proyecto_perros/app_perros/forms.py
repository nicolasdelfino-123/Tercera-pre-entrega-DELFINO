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
    GENERO_CHOICES = (
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    )
    nombre = forms.CharField(label="Nombre", max_length=64)
    tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)
    fecha_entrada = forms.DateField()
    foto = forms.ImageField(label="Foto", required=False)
    #campos extras ver_mas
    edad = forms.ChoiceField(label="Edad", choices=((str(i), str(i)) for i in range(1, 30)))
    raza = forms.ChoiceField(label="Raza", choices=GENERO_CHOICES)
    genero = forms.CharField(label="Género", max_length=10)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    

    def __init__(self, *args, **kwargs):
        super(PerroFormulario, self).__init__(*args, **kwargs)
        self.fields['foto'].widget.attrs['accept'] = 'image/*'
        

class AdoptanteFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256) 
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=32)
    fecha_nacimiento = forms.DateField()
    
    
class AdopcionFormulario(forms.Form):
    adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.all())
    perro = forms.ModelChoiceField(queryset=Perro.objects.exclude(adopcion__isnull=False))
    
    
