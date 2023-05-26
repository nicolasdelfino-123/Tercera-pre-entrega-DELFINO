from django import forms
from app_perros.models import Adoptante, Perro

# formulario busqueda
class BuscarPerro(forms.Form):
    TAMANIO_CHOICES = (
        ('chico', 'Chico'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
        ('VER TODOS', 'VER TODOS'),  # Opción para mostrar todos los perros
    )
    tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)


class PerroFormulario(forms.ModelForm):
    TAMANIO_CHOICES = (
        ('chico', 'Chico'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    )
    GENERO_CHOICES = (
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    )

    tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)
    genero = forms.ChoiceField(label="Género", choices=GENERO_CHOICES)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    edad = forms.IntegerField(label="Edad", min_value=0, max_value=25)
    class Meta:
        model = Perro
        fields = ['nombre', 'tamanio', 'fecha_entrada', 'foto', 'edad', 'raza', 'genero', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'tamanio': 'Tamaño',
            'fecha_entrada': 'Fecha de Entrada',
            'foto': 'Foto',
            'edad': 'Edad',
            'raza': 'Raza',
            'genero': 'Género',
            'descripcion': 'Descripción',
        }
        widgets = {
            'foto': forms.ClearableFileInput(attrs={'accept': 'image/*'})
        }
        
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')

        if nombre:
            cleaned_data['nombre'] = nombre.capitalize()
  
        return cleaned_data
   
    
class AdoptanteFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256) 
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=32)
    fecha_nacimiento = forms.DateField()



class AdopcionFormulario(forms.Form):
    adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.none())
    perro = forms.ModelChoiceField(queryset=Perro.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        perros_disponibles = kwargs.pop('perros_disponibles')
        super(AdopcionFormulario, self).__init__(*args, **kwargs)
        self.fields['adoptante'].queryset = Adoptante.objects.filter(creador=user)
        self.fields['perro'].queryset = perros_disponibles



    
    
