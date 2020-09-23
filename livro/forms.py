from django.forms import ModelForm
from .models import Livro
from autor.models import Autor

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor','quantidade_de_paginas', 'preco']
