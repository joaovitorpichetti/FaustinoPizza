from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from FaustinoPizza.funcoes import usuario_esta_no_grupo
from vendas.mixins import UsuarioEAdministrador
from vendas.models.categoria import Categoria

grupo_padrao = 'Administrador'

'''def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, "categorias.html", context)'''

class CategoriaListView(UsuarioEAdministrador, ListView): #O UserPassesTestMixin vai verificar sobre as permisções
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'


class CategoriaCreateView(UserPassesTestMixin, CreateView):
    model = Categoria
    template_name = 'categoria_criar.html'
    context_object_name = 'categoria'
    fields = '__all__' #aqui vai os campos do Forms, não  precisa criar.

    def get_success_url(self):
        return reverse('vendas:categoria_lista')

    def test_func(self):
        return usuario_esta_no_grupo(self.request.user, 'Administrador') or self.request.user.is_staff

class CategoriaUpdateView(UserPassesTestMixin, UpdateView):
    model = Categoria
    template_name = 'categoria_editar.html'
    context_object_name = 'categoria'
    fields = '__all__'

    def get_success_url(self):
        return reverse('vendas:categoria_lista') #aqui se der sucesso vai mandar para a URL de listagem

    def test_func(self):
        return usuario_esta_no_grupo(self.request.user, 'Administrador') or self.request.user.is_staff

class CategoriaDeleteView(UsuarioEAdministrador, DeleteView):
    model = Categoria
    template_name = 'categoria_excluir.html'

    def get_success_url(self):
        return reverse('vendas:categoria_lista')

