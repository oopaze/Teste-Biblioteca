from django.test import TestCase
from livro.models import Livro
from autor.models import Autor
from decimal import Decimal

class TestModelLivro(TestCase):
    def setUp(self):
       self.autor = Autor(nome='Pedro')
       self.livro = Livro(nome="O livro", autor=self.autor, quantidade_de_paginas=300, preco=Decimal('39.90'))

    def test_str(self):
        """Transforming Livro into Str should return Livro.nome"""
        esperado = "O livro"
        resultado = str(self.livro)

        self.assertEqual(esperado, resultado)
