from django.test import TestCase
from autor.models import Autor

class TestModelAutor(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nome='Pedro')

    def test_autor_atributes(self):
        """An autor always has nome atribute"""
        self.assertTrue(hasattr(Autor, 'nome'))
    
    def test_create_autor(self):
        self.assertIsNotNone(self.autor)

    def test_str_return_nome(self):
        """Transform autor into str returns autor name"""
        esperado = 'Pedro'
        resultado = str(self.autor)

        self.assertEqual(esperado, resultado)

