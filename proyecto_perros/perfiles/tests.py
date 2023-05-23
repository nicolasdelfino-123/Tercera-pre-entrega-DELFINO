from django.test import TestCase

# Create your tests here.
from django.db import IntegrityError
from app_perros.models import Perro


class PerroTests(TestCase):
    """En esta clase van todas las pruebas del modelo Curso."""

    def test_creacion_perro(self):
        # caso uso esperado
        perro = Perro(nombre="Titulo", edad=20)
        perro.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Perro.objects.count(), 1)
        self.assertEqual(Perro.nombre, "Titulo")
        self.assertEqual(Perro.comision, 1000)

    def test_perro_str(self):
        perro = Perro(nombre="nico", edad=20)
        perro.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(perro.__str__(), "nico | 20")