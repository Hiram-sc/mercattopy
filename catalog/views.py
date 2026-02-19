from django.http import HttpResponse

from django.shortcuts import render
from catalog.models import Categoria, Produto

def lista_categoria(request):
    categorias = Categoria.objects.all()
    return HttpResponse(categorias)

def lista_produto(request):
    produtos = Produto.objects.all()
    return HttpResponse(produtos)

def item_produto(request, id):
    item = Produto.objects.get(id=id)
    return HttpResponse(item)