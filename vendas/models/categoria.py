from .base import BaseModel
from django.db import models

class Categoria(BaseModel):
    nome_categoria = models.CharField(verbose_name='Nome da categoria', max_length=50)

    class Meta:
        abstract = False
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome_categoria
