from usuarios.models.base import BaseModel
from django.db import models

class Endereco(BaseModel):
    cep = models.CharField(verbose_name='CEP', max_length=15)
    logradouro = models.CharField(verbose_name='Logradouro', max_length=50)
    numero = models.CharField(verbose_name='Numero', max_length=5)
    complemento = models.CharField(verbose_name='Complemento', max_length=15, blank=True, null=True) #Blank True aceita formulario sem dados e Null True aceita Null no DB
    bairro = models.CharField(verbose_name='Bairro', max_length=20)
    cidade = models.CharField(verbose_name='Cidade', max_length=20)
    estado = models.CharField(verbose_name='Estado', max_length=20)
    uf = models.CharField(verbose_name='UF', max_length=2, null=True, blank=True)

    class Meta:
        abstract = False
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.cep + ' - ' + self.logradouro + ' - ' + self.numero + ' - ' + self.bairro + ' - ' + self.cidade + ' - ' + self.estado
