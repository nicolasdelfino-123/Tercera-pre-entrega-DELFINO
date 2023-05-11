from django.db import models
import __future__
from django.db import models


class Perro(models.Model):
    nombre = models.CharField(max_length= 64)
    tamanio = models.CharField(max_length=100)
    fecha_entrada=models.DateField(auto_now=False)

    def __str__(self):
        return f"{self.nombre} | {self.tamanio}"


class Adoptante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()
    
    # Contacto
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
   

    def __str__(self):
        return f"{self.nombre}, {self.apellido}" 
        

class Adopcion(models.Model):
    adoptante = models.ForeignKey(Adoptante, on_delete=models.SET_NULL,blank=True,null=True)
    perro = models.ForeignKey(Perro, blank=True, null=True, on_delete=models.PROTECT)
    fecha_adopcion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.adoptante} adoptó el perro {self.perro}"
        
    

    

    
   
        