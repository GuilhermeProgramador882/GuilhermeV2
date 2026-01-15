from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('nova/', views.criar_movimentacao, name='criar_movimentacao'),
    path('editar/<int:id>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('excluir/<int:id>/', views.excluir_movimentacao, name='excluir_movimentacao'),
]
