from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.lista_categoria),
    path('produtos/', views.lista_produto),
    path('produtos/<int:id>/', views.item_produto)
]
