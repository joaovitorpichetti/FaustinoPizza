from django.contrib import admin
from vendas.models.categoria import Categoria
from vendas.models.produto import Produto
from vendas.models.item import Item
from vendas.models.pagamento import Pagamento
from vendas.models.pedido import Pedido

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Pagamento)
admin.site.register(Pedido)
