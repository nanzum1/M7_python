from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Datos iniciales para todas las pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Alfa", 
            ciudad="Santiago", 
            pais="Chile"
        )
        cls.director = DirectorGeneral.objects.create(
            nombre="Dr. Juan Pérez", 
            laboratorio=cls.laboratorio,
            especialidad="Química"
        )
        cls.producto = Producto.objects.create(
            nombre="Producto X",
            laboratorio=cls.laboratorio,
            f_fabricacion="2020-05-01",
            p_costo=1000.00,
            p_venta=1500.00
        )

    def test_datos_iniciales(self):
        """Verificar que los datos iniciales creados coincidan con los definidos en setUpTestData para Laboratorio"""
        laboratorio = Laboratorio.objects.get(nombre="Laboratorio Alfa")
        director = DirectorGeneral.objects.get(nombre="Dr. Juan Pérez")
        producto = Producto.objects.get(nombre="Producto X")

        self.assertEqual(laboratorio.nombre, "Laboratorio Alfa")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")
        self.assertEqual(director.nombre, "Dr. Juan Pérez")
        self.assertEqual(director.especialidad, "Química")
        self.assertEqual(producto.nombre, "Producto X")
        self.assertEqual(producto.laboratorio, laboratorio)
        self.assertEqual(producto.f_fabricacion.strftime("%Y-%m-%d"), "2020-05-01")
        self.assertEqual(producto.p_costo, 1000.00)
        self.assertEqual(producto.p_venta, 1500.00)

    def test_urls_http_200(self):
        """Verificar que la URL para el laboratorio devuelva HTTP 200"""
        response_laboratorio = self.client.get(reverse('ver_laboratorio', args=[self.laboratorio.id]))
        
        # Verifica que la URL de la vista del laboratorio devuelva un código de estado 200
        self.assertEqual(response_laboratorio.status_code, 200)

    def test_plantillas_correctas(self):
        """Verificar que se use la plantilla correcta y que el contenido HTML contenga los datos esperados"""
        response_laboratorio = self.client.get(reverse('ver_laboratorio', args=[self.laboratorio.id]))

        # Verifica que se esté usando la plantilla correcta
        self.assertTemplateUsed(response_laboratorio, 'ver_laboratorio.html')
        
        # Verifica que el contenido de la página contiene el nombre y los detalles del laboratorio
        self.assertContains(response_laboratorio, "Laboratorio Alfa")
        self.assertContains(response_laboratorio, "Santiago")
        self.assertContains(response_laboratorio, "Chile")
