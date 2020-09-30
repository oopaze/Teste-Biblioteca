from django.test import TestCase, Client
from django.urls import reverse

from decimal import Decimal

from autor.models import Autor


class TestAddBook(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nome='Pedro')

        self.adicionar_url = reverse('adicionar_livro')

    def test_create_book(self): 
        """Create Livro should redirect to /livro/"""
        data = {
            'nome': 'O Livro',
            'autor': 1,
            'quantidade_de_paginas': 300,
            'preco': Decimal('39.90')
        }

        response = self.client.post(self.adicionar_url, data)

        self.assertEquals(response.status_code, 302)    

    def test_create_book_with_invalid_data(self):
        """Create livro sending an invalid data returns status code 200 on livro/adicionar_html"""
        data = {}
        response = self.client.post(self.adicionar_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'livro/adicionar.html')

    def test_template(self):
        """GET /livro/adicionar/ should use livro/adicionar.html as its template"""
        response = self.client.get(self.adicionar_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'livro/adicionar.html')
    
    def test_form_tags_in_html(self):
        """Template livro/adicionar.html must have some specific tags"""
        response = self.client.get(self.adicionar_url)

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
