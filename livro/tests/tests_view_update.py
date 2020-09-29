from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal

from autor.models import Autor

class TestUpdateBook(TestCase):
    def setUp(self):
        self.client = Client()
        self.autor = Autor.objects.create(nome='Pedro')
        self.atualizar_url = reverse('atualizar_livro', args=[1])

        self.client.post(reverse('adicionar_livro'),  {
            'nome': 'O Livro',
            'autor': 1,
            'quantidade_de_paginas': 300,
            'preco': Decimal('39.90')
        })
        
    def test_update_book(self):
        """Update a book always response status_code 302 (redirect)"""
        data = {
            'nome': 'Os Livros',
            'autor': 1,
            'quantidade_de_paginas': 299,
            'preco': Decimal('39.90')
        }
        response = self.client.post(self.atualizar_url, data)

        self.assertEquals(response.status_code, 302)

    def test_update_book_with_invalid_data(self):
        """Update book without sending an invalid data shouldn't redirect to /livro/"""
        data = {}
        response = self.client.post(self.atualizar_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'livro/atualizar.html')
    
    def test_template(self):
        """GET /livro/atualizar/ should use livro/atualizar.html as its template"""
        response = self.client.get(self.atualizar_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'livro/atualizar.html')

    def test_form_tags_in_html(self):
        """Template livro/atualizar.html must have some specific tags"""
        response = self.client.get(self.atualizar_url)

        tags = (
            ('<form', 1),
            ('<select', 1),
            ('<input', 4),
            ('type="text"', 1),
            ('type="submit"', 1),
            ('type="number"', 2)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(response, text, count)
