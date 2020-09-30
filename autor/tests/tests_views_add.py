from django.test import TestCase
from django.urls import reverse

class TestAddAutor(TestCase):
    def setUp(self):
        self.adicionar_url = reverse('adicionar_autor')

    def test_create(self):
        """Create Autor always return status code 302"""
        data = {'nome':'José Pedro'}
        response = self.client.post(self.adicionar_url, data)

        self.assertEquals(response.status_code, 302)

    def test_create_autor_with_invalid_data(self):
        """Create autor sending an invalid data returns status code 200 on autor/adicionar_html"""
        data = {'name':'José Pedro'}
        response = self.client.post(self.adicionar_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/adicionar.html')

    def test_template(self):
        """GET /autor/adicionar/ should use autor/adicionar.html as its template"""
        response = self.client.post(self.adicionar_url)

        self.assertTemplateUsed(response, 'autor/adicionar.html')

    def test_form_tags_in_html(self):
        """Template autor/adicionar.html must have some specific tags"""
        response = self.client.get(self.adicionar_url)

        tags = (
            ('<form', 1),
            ('<input', 2),
            ('type="text"', 1),
            ('type="submit"', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(response, text, count)


