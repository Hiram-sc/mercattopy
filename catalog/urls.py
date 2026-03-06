from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.lista_categoria, name='categoria'),
    path('produto/', views.lista_produto, name='produto'),
    path('produto/<int:id>/excluir', views.excluir_produto, name='product_delete'),
    path('produto/novo/', views.criar_produto, name='product_add'),
    path('produto/<int:id>/', views.item_produto, name='product_detail'),
    path('produto/<int:id>/editar', views.editar_produto, name='product_edit')
]
