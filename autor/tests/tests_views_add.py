from django.test import TestCase, Client
from django.urls import reverse

class TestAddAutor(TestCase):
    def setUp(self):
        self.client = Client()
        self.adicionar_url = reverse('adicionar_autor')

    def test_create(self):
        data = {'nome':'José Pedro'}
        response = self.client.post(self.adicionar_url, data)

        self.assertEquals(response.status_code, 302)

    def test_create_autor_with_invalid_data(self):
        data = {'name':'José Pedro'}
        response = self.client.post(self.adicionar_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/adicionar.html')

    def test_template(self):
        response = self.client.post(self.adicionar_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/adicionar.html')

    def test_form_tags_in_html(self):
        response = self.client.get(self.adicionar_url)

        tags = (
            ('<form', 1),
            ('<input', 2)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(response, text, count)


