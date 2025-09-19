from django.contrib import admin
from usuarios.models.colaborador import Colaborador
from usuarios.models.endereco import Endereco
from usuarios.models.cliente import Cliente

# Register your models here.

admin.site.register(Colaborador)
admin.site.register(Endereco)
admin.site.register(Cliente)
