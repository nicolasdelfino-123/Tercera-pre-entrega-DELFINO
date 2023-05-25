####formulario nuevo
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

class AdoptanteFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256) 
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=32)
    fecha_nacimiento = forms.DateField()



# class AdopcionFormulario(forms.Form):
#     adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.none())
#     perro = forms.ModelChoiceField(queryset=Perro.objects.all())

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user')
#         super(AdopcionFormulario, self).__init__(*args, **kwargs)
#         self.fields['adoptante'].queryset = Adoptante.objects.filter(creador=user)


# class AdopcionFormulario(forms.Form):
#     adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.none())
#     perro = forms.ModelChoiceField(queryset=None)

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user')
#         perros_disponibles = kwargs.pop('perros_disponibles')
#         super(AdopcionFormulario, self).__init__(*args, **kwargs)
#         self.fields['adoptante'].queryset = Adoptante.objects.filter(creador=user)
#         self.fields['perro'].queryset = perros_disponibles

class AdopcionFormulario(forms.Form):
    adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.none())
    perro = forms.ModelChoiceField(queryset=Perro.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        perros_disponibles = kwargs.pop('perros_disponibles')
        super(AdopcionFormulario, self).__init__(*args, **kwargs)
        self.fields['adoptante'].queryset = Adoptante.objects.filter(creador=user)
        self.fields['perro'].queryset = perros_disponibles


# class AdopcionFormulario(forms.Form):
#     pass



####formulario viejo#####

# from django import forms
# from app_perros.models import Adoptante, Perro

# # formulario busqueda 

# class BuscarPerro(forms.Form):
#      TAMANIO_CHOICES = (
#         ('chico', 'Chico'),
#         ('mediano', 'Mediano'),
#         ('grande', 'Grande'),
#     )
#      tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)
    

# class PerroFormulario(forms.Form):
#     TAMANIO_CHOICES = (
#         ('chico', 'Chico'),
#         ('mediano', 'Mediano'),
#         ('grande', 'Grande'),
#     )
#     nombre = forms.CharField(label="Nombre", max_length=64)
#     tamanio = forms.ChoiceField(label="Tamaño", choices=TAMANIO_CHOICES)
#     fecha_entrada = forms.DateField()
#     foto = forms.ImageField(label="Foto", required=False)
#     #campos extras ver_mas
#     edad = forms.ChoiceField(label="Edad", choices=((str(i), str(i)) for i in range(1, 20)))
#     raza = forms.CharField(max_length=100)
#     genero = forms.CharField(label="Género", max_length=10)
#     descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    

#     def __init__(self, *args, **kwargs):
#         super(PerroFormulario, self).__init__(*args, **kwargs)
#         self.fields['foto'].widget.attrs['accept'] = 'image/*'
        

    
# class AdoptanteFormulario(forms.Form):
#     apellido = forms.CharField(max_length=256)
#     nombre = forms.CharField(max_length=256) 
#     email = forms.EmailField()
#     telefono = forms.CharField(max_length=20)
#     dni = forms.CharField(max_length=32)
#     fecha_nacimiento = forms.DateField()
    
    
# class AdopcionFormulario(forms.Form):
#     adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.all())
#     perro = forms.ModelChoiceField(queryset=Perro.objects.exclude(adopcion__isnull=False))
    
    
