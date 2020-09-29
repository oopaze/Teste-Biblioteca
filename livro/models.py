from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator

from datetime import datetime

from autor.models import Autor


class Livro(models.Model):
    nome = models.CharField("nome", max_length=100, null=False, blank=False, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    quantidade_de_paginas = models.PositiveIntegerField(
                                        "quantidade_de_paginas",
                                        null=False,
                                        blank=False,
                                    )
                                                
    preco = models.DecimalField("preco",
                               null=False,
                               blank=False,
                               decimal_places=2,
                               max_digits=6,
                               validators=[
                                    MinValueValidator(
                                        Decimal('0.01'),
                                        message='Preço deve ser maior que 0.'
                                    ),
                               ])
    data_de_inclusao = models.DateField("data_de_inclusao", default=datetime.now, editable=False)

    def __str__(self):
        return self.nome