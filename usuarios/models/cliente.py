from django.contrib.auth.models import User
from usuarios.models.base import BaseModel
from usuarios.models.endereco import Endereco
from django.db import models

class Cliente(BaseModel):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    telefone = models.CharField(verbose_name='Telefone', max_length=20)
    cpfcnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=20, blank=True, null=True)
    enderecos = models.ManyToManyField(Endereco)

    class Meta:
        abstract = False
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self):
        return self.usuario.first_name + ' ' + self.usuario.last_name + ' Tel: ' + self.telefone
