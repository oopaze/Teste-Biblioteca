from django.test import TestCase, Client
from django.urls import reverse

class TestUpdateAutor(TestCase):
    def setUp(self):
        self.atualizar_url = reverse('atualizar_autor', args=[1])

        self.client.post(reverse('adicionar_autor'), {'nome':'Pedro'})

    def test_update(self):
        """Update a autor always response status_code 302 (redirect)"""
        data = {'nome':'José Pedro'}
        response = self.client.post(self.atualizar_url, data)

        self.assertEquals(response.status_code, 302)

    def test_update_autor_with_invalid_data(self):
        """Update autor sending an invalid data returns status code 200 on /autores/atualizar/"""
        data = {'name':'José Pedro'}
        response = self.client.post(self.atualizar_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/atualizar.html')

    def test_update_unexistent_autor(self): 
        """Update unexistent autor return status code 404(Not foudn)"""
        atualizar_url = reverse('atualizar_autor', args=[2])

        response = self.client.post(atualizar_url)

        self.assertEquals(response.status_code, 404)
    
    def test_template(self):
        """GET /autores/atualizar/ should use autor/atualizar.html as its template"""
        response = self.client.get(self.atualizar_url)

        self.assertTemplateUsed(response, 'autor/atualizar.html')

    def test_form_tags_in_html(self):
        """Template autor/atualizar.html must have some specific tags"""
        response = self.client.get(self.atualizar_url)

        tags = (
            ('<form', 1),
            ('<input', 2),
            ('type="text"', 1),
            ('type="submit"', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(response, text, count)
