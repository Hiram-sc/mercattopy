from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.lista_categoria, name='category_list'),
    path('produtos/', views.lista_produto, name='product_list'),
    path('produtos/<int:id>/', views.item_produto, name='product_detail')
]
