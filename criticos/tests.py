
from django.test import TestCase
from django.urls import reverse
from .models import Restaurante
# Create your tests here.



class RestauranteTests(TestCase):
    def test_agregar_restaurante(self):
        response = self.client.post(
            reverse('agregar_restaurante'),
            {
                'nombre': 'Restaurante Ejemplo',
                'direccion': '123 Calle Principal',
                'telefono': '555-1234',
                'descripcion': 'Un lugar para disfrutar de deliciosas comidas.',
            }
        )
        self.assertEqual(response.status_code, 302)  # Debe redirigir después de agregar
        self.assertEqual(Restaurante.objects.count(), 1)  # Debe haber un restaurante en la base de datos