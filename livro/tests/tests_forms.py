from django.test import TestCase
from livro.forms import LivroForm

class TestFormLivro(TestCase):
    def setUp(self):
        self.form = LivroForm()

    def test_fields(self):
        """
        LivroForm must have all fields bellow:
            nome, autor, quantidade_de_paginas, preco
        """

        expected = ['nome', 'autor', 'quantidade_de_paginas', 'preco']

        self.assertSequenceEqual(expected, list(self.form.fields))