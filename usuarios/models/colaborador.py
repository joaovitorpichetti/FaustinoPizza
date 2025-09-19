from django.contrib.auth.models import User
from usuarios.models.endereco import Endereco
from usuarios.models.base import BaseModel
from django.db import models

class Colaborador(BaseModel):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    cpf_colaborador = models.CharField(max_length=20, verbose_name='CPF do Colaborador', unique=True)
    telefone_colaborador = models.CharField(max_length=20, verbose_name='Telefone do Colaborador')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, verbose_name='Endereço')

    class Meta:
        abstract = False
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.usuario.first_name + " - " + self.usuario.last_name
