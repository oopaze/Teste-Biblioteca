from django.test import TestCase, Client
from django.urls import reverse

class TestUpdateAutor(TestCase):
    def setUp(self):
        self.client = Client()
        self.atualizar_url = reverse('atualizar_autor', args=[1])

        self.client.post(reverse('adicionar_autor'), {'nome':'Pedro'})

    def test_update(self):
        data = {'nome':'José Pedro'}
        response = self.client.post(self.atualizar_url, data)

        self.assertEquals(response.status_code, 302)

    def test_update_autor_with_invalid_data(self):
        data = {'name':'José Pedro'}
        response = self.client.post(self.atualizar_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/atualizar.html')

    def test_template(self):
        response = self.client.get(self.atualizar_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/atualizar.html')

    def test_form_tags_in_html(self):
        response = self.client.get(self.atualizar_url)

        tags = (
            ('<form', 1),
            ('<input', 2)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(response, text, count)

    def test_update_unexistent_autor(self):
        atualizar_url = reverse('atualizar_autor', args=[2])

        response = self.client.post(atualizar_url)

        self.assertEquals(response.status_code, 404)