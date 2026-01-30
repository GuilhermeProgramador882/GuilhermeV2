from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacao/nova/', views.criar_movimentacao, name='criar_movimentacao'),
    path('movimentacao/editar/<int:id>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('movimentacao/excluir/<int:id>/', views.excluir_movimentacao, name='excluir_movimentacao'),
    
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categoria/nova/', views.criar_categoria, name='criar_categoria'),
    path('categoria/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
]
