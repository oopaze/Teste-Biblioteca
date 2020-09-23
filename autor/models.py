from django.db import models

class Autor(models.Model):
    nome = models.CharField("nome", unique=True, null=False, max_length=50, blank=False)

    def __repr__(self):
        return f"< Autor {self.nome} >"

    def __str__(self):
        return self.nome
