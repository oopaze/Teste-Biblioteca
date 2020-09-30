from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal

from autor.models import Autor


class TestDeletBook(TestCase):
    def setUp(self):
        self.client = Client()
        self.deletar_url = reverse('deletar_livro', args=[1])
        
        self.autor = Autor.objects.create(nome='Pedro')

        self.client.post(reverse('adicionar_livro'), {
            'nome': 'O Livro',
            'autor': 1,
            'quantidade_de_paginas': 300,
            'preco': Decimal('39.90')
        })

    def test_template(self):
        """GET /livro/deletar/ should use livro/deletar.html as its template"""
        response = self.client.get(self.deletar_url)

        self.assertTemplateUsed(response, 'livro/deletar.html')

    def test_deletar_livro(self):
        """Delete a book always response status_code 302 (redirect)"""
        response = self.client.post(self.deletar_url)

        self.assertEquals(response.status_code, 302)

    def test_delete_unexistent_book(self):
        """Delete unexistent livro return status code 404(Not foudn)"""
        deletar_url = reverse('deletar_livro', args=[2])

        response = self.client.post(deletar_url)

        self.assertEquals(response.status_code, 404)

