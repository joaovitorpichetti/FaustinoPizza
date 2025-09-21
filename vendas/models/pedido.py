from .base import BaseModel
from django.db import models
from .pagamento import Pagamento
from .produto import Produto
from usuarios.models.cliente import Cliente

class Pedido(BaseModel):

    class StatusChoices(models.TextChoices):
        AGUARDANDO_CONFIRMACAO = 'AGC', 'Aguardando Confirmação'  # O pedido foi feito, mas a cozinha ainda não o aceitou
        RECEBIDO = 'REC', 'Recebido'  # A cozinha confirmou e o item entrará em preparo
        EM_PREPARO = 'PRE', 'Em Preparo'  # A pizza está sendo feita
        PRONTO_PARA_ENTREGA = 'PRO', 'Pronto para Entrega'  # A pizza está pronta, aguardando o entregador
        A_CAMINHO = 'CAM', 'A Caminho'  # O entregador saiu com o pedido
        ENTREGUE = 'ENT', 'Entregue'  # O cliente recebeu o pedido
        CANCELADO = 'CAN', 'Cancelado'  # O pedido foi cancelado

    class EntregaChoices(models.TextChoices):
        DELIVERY = 'DEL', 'Delivery'  # Para entregar no endereço do cliente
        RETIRADA = 'RET', 'Retirada no Local'  # Cliente busca na pizzaria


    produtos = models.ManyToManyField(Produto, verbose_name='Informe os produtos do pedido')
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    status_pedido = models.CharField(choices=StatusChoices.choices, max_length=3, verbose_name='Status do pedido', default=StatusChoices.AGUARDANDO_CONFIRMACAO)
    entrega = models.CharField(choices=EntregaChoices.choices, max_length=3, verbose_name='Entrega')
    valor = models.FloatField(verbose_name='Valor', blank=True, null=True)
    forma_pagamento = models.OneToOneField(Pagamento, verbose_name='Forma de pagamento', on_delete=models.PROTECT)
    data_hora = models.DateTimeField(verbose_name='Data/hora', auto_now_add=True)

    class Meta:
        abstract = False
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{self.cliente.__str__()} - {self.status_pedido} - {self.data_hora}'
