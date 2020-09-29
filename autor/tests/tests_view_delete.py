from django.test import TestCase, Client
from django.urls import reverse


class TestDeleteAutor(TestCase):
    def setUp(self):
        self.client = Client()
        self.deletar_url = reverse('deletar_autor', args=[1])
        
        self.client.post(reverse('adicionar_autor'), {'nome':'Pedro'})
    
    def test_delete(self):
        response = self.client.post(self.deletar_url)

        self.assertEquals(response.status_code, 302)

    def test_delete_unexistent_autor(self):
        deletar_url = reverse('deletar_autor', args=[2])

        response = self.client.post(deletar_url)

        self.assertEquals(response.status_code, 404)

    def test_template(self):
        response = self.client.get(self.deletar_url)

        self.assertTemplateUsed(response, 'autor/deletar.html')

