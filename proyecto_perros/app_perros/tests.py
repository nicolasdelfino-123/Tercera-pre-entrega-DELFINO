from django.test import TestCase
from .models import Perro

from django.utils import timezone


class PerroTests(TestCase):
    """En esta clase van todas las pruebas del modelo Perro."""

    def test_creacion_perro(self):
        # Caso de uso esperado
        perro = Perro(nombre="Max", raza="Bulldog", edad= 5, fecha_entrada=timezone.now())
        perro.save()

        # Compruebo que el perro fue creado y la data fue guardada correctamente
        self.assertEqual(Perro.objects.count(), 1)
        self.assertEqual(perro.nombre, "Max")
        self.assertEqual(perro.raza, "Bulldog")
        self.assertEqual(perro.edad, 5)
