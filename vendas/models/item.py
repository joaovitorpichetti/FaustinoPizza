from django.core.validators import MinValueValidator

from vendas.models.base import BaseModel
from django.db import models

class Item(BaseModel):
    nome_item = models.CharField(verbose_name='Nome de item', max_length=50)
    valor_item = models.DecimalField(verbose_name='Valor de item', decimal_places=2, max_digits=10, validators=[MinValueValidator(0.01)]) # validators Garante que o valor seja positivo

    class Meta:
        abstract = False
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.nome_item
