from .base import BaseModel
from django.db import models

class Pagamento(BaseModel):
    #status_pagamento
    class StatusChoices(models.TextChoices):
        PENDENTE = 'PEN', 'Pendente'
        APROVADO = 'APR', 'Aprovado'
        RECUSADO = 'REC', 'Recusado'
        CANCELADO = 'CAN', 'Cancelado'
        EM_PROCESSAMENTO = 'PRO', 'Em Processamento'
        REEMBOLSADO = 'REE', 'Reembolsado'


    #forma_pagamento
    class FormaPagamentoChoices(models.TextChoices):
        """
        Define as opções para a forma de pagamento.
        O primeiro valor é o que será armazenado no banco de dados.
        O segundo valor é o que será exibido para o usuário.
        """
        DINHEIRO = 'DIN', 'Dinheiro'
        PIX = 'PIX', 'Pix'
        CARTAO_CREDITO = 'CC', 'Cartão de Crédito'
        CARTAO_DEBITO = 'CD', 'Cartão de Débito'
        #OUTRO = 'OUT', 'Outro'

    status_pagamento = models.CharField(choices=StatusChoices.choices, max_length=3, verbose_name='Status de pagamento')
    forma_pagamento = models.CharField(choices=FormaPagamentoChoices.choices, max_length=3, verbose_name='Forma de pagamento')


    class Meta:
        abstract = False
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
