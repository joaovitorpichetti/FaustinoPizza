from django.views.generic import ListView, CreateView
from vendas.mixins import UsuarioEAdministrador
from vendas.models.produto import Produto

class ProdutoListView(UsuarioEAdministrador, ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'

class ProdutoCreateView(UsuarioEAdministrador, CreateView):
    model = Produto
    template_name = 'produto_criar.html'
    context_object_name = 'produto'
    fields = '__all__'
