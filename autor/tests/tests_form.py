from django.test import TestCase
from autor.forms import AutorForm

class TestFormLivro(TestCase):
    def setUp(self):
        self.form = AutorForm()

    def test_fields(self):
        """
        AutorForm must have all fields bellow:
            nome
        """

        expected = ['nome']

        self.assertSequenceEqual(expected, list(self.form.fields))