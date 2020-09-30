from django.test import TestCase
from livro.models import Livro
from autor.models import Autor
from decimal import Decimal

class TestModelLivro(TestCase):
    def setUp(self):
       self.autor = Autor.objects.create(nome='Pedro')
       self.livro = Livro.objects.create(
                        nome="O livro",
                        autor=self.autor, 
                        quantidade_de_paginas=300, 
                        preco=Decimal('39.90')
                    )

    def test_livro_atributes(self):
        """
        A livro always has these attributes: 
                nome, 
                autor, 
                quantidade_de_paginas, 
                preco,
                data_de_inclusao
        """
        fields = (
            ('nome'),
            ('autor'),
            ('quantidade_de_paginas'),
            ('preco'),
            ('data_de_inclusao')
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Livro, field))

    def test_create_livro(self):
        self.assertIsNotNone(self.livro)

    def test_str(self):
        """Transforming Livro into Str should return Livro.nome"""
        esperado = "O livro"
        resultado = str(self.livro)

        self.assertEqual(esperado, resultado)
