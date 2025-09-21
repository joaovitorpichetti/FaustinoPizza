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
        # 1. Acessamos a LISTA de objetos Categoria com .all()
        categorias_do_produto = self.categorias.all()

        # 2. Verificamos se a lista não está vazia de forma eficiente com .exists()
        if categorias_do_produto.exists():
            # 3. Criamos uma lista SÓ COM OS NOMES de cada categoria
            #    Exemplo de resultado: ['Pizzas', 'Promoção de Terça']
            lista_de_nomes = [categoria.__str__() for categoria in categorias_do_produto]

            # 4. Juntamos os nomes da lista em um único texto, separados por ", "
            #    Exemplo de resultado: "Pizzas, Promoção de Terça"
            nomes_formatados = ", ".join(lista_de_nomes)

            return f'{self.nome_produto} - [{nomes_formatados}]'
        else:
            # 5. Se a lista de categorias estiver vazia, mostramos a mensagem padrão
            return f'{self.nome_produto} - (Sem Categoria)'
