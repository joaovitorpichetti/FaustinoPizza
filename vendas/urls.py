from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('categorias', views.CategoriaListView.as_view(), name='categoria_lista'),
    path('categorias/criar', views.CategoriaCreateView.as_view(), name='categoria_criar'),
    path('categorias/editar/<int:pk>', views.CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categorias/excluir/<int:pk>', views.CategoriaDeleteView.as_view(), name='categoria_excluir'),
]
