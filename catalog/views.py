from django.shortcuts import render
from catalog.models import Categoria, Produto

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def logout_view(request):
    return render(request, 'auth/login.html')

def lista_categoria(request):
    categories = Categoria.objects.all()
    return render(request, "catalog/category_list.html", {"categories" : categories})

def lista_produto(request):
    products = Produto.objects.all()
    return render(request, "catalog/product_list.html", {"products" : products})

def item_produto(request, id):
    product = Produto.objects.get(id=id)
    return render(request, "catalog/product_detail.html", {"product" : product})