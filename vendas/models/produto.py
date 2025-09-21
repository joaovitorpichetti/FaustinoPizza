from django.core.validators import MinValueValidator
from .base import BaseModel
from .item import Item
from .categoria import Categoria
from django.db import models

class Produto(BaseModel):
    img_produto = models.ImageField(verbose_name='Imagem do produto')
    nome_produto = models.CharField(verbose_name='Nome do produto', max_length=100)
    descricao_produto = models.TextField(verbose_name='Descrição do Produto', max_length=500, blank=True)
    valor_produto = models.DecimalField(verbose_name='Valor do Produto', max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    itens = models.ManyToManyField(Item, verbose_name='Itens do Produto', blank=True)
    categorias = models.ManyToManyField(Categoria, verbose_name='Categorias do Produto')

    class Meta:
        abstract = False
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome_produto + ' - ' + self.categorias.__str__()

