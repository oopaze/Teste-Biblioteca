from django.contrib import admin
from django.urls import path
from .views import exibir_livros, adicionar_livro, atualizar_livro, deletar_livro

urlpatterns = [
    path('', exibir_livros, name='exibir_livros'),
    path('adicionar/', adicionar_livro, name='adicionar_livro'),
    path('atualizar/<int:id>', atualizar_livro, name='atualizar_livro'),
    path('deletar/<int:id>', deletar_livro, name='deletar_livro'),
]
