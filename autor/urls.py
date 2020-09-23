from django.contrib import admin
from django.urls import path
from .views import (exibir_autor, criar_autor,
                    deletar_autor, atualizar_autor)

urlpatterns = [
    path('', exibir_autor, name="exibir_autor"),
    path('criar/', criar_autor, name="criar_autor"),
    path('atualizar/<int:id>', atualizar_autor, name="atualizar_autor"),
    path('deletar/<int:id>', deletar_autor, name="deletar_autor"),
]
