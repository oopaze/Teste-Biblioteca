from django.test import TestCase
from autor.models import Autor

class TestModelAutor(TestCase):
    def setUp(self):
        self.autor = Autor(nome='Pedro')

    def teste_str_retorna_nome(self):
        esperado = 'Pedro'
        resultado = str(self.autor)

        self.assertEqual(esperado, resultado)

