from django.contrib.auth.models import User
from .base import BaseModel
from .endereco import Endereco
from django.db import models

class Cliente(BaseModel):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    telefone = models.CharField(verbose_name='Telefone', max_length=20)
    cpfcnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=20, blank=True, null=True)
    enderecos = models.ManyToManyField(Endereco, blank=True, null=True, verbose_name='Endereços')

    class Meta:
        abstract = False
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self):
        return self.usuario.first_name + ' ' + self.usuario.last_name + ' Tel: ' + self.telefone
