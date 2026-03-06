from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.registrar_venda, name='vendas')
]