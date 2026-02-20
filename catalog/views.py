from django.contrib import messages
from django.shortcuts import render, redirect
from catalog.forms import ProdutoForm
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


def criar_produto(request):
        if request.method == "POST":
            form = ProdutoForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Produto criado com sucesso.")
                return redirect("lista_produto")
            
            else:
                messages.error(request, "Erro ao criar o produto. Verifique os dados.")
        
        else:
            form = ProdutoForm()

        products = Produto.objects.all()
        return render(request, "catalog/product_list.html", {"products" : products, "form" : form})


def editar_produto(request, id):
    product = Produto.objects.get(id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("lista_produto")
        
    else:
        form = ProdutoForm(instance=product)

    products = Produto.objects.all()

    return render(request, "catalog/product_list.html", {
        "form" : form,
        "products" : products
    })


def deletar_produto(request, id):
    product = Produto.objects.get(id=id)
    
    if product.quantidade_estoque > 0:
        messages.error(request, "Não é possível excluir produto com estoque maior que zero.")
        return redirect("item_produto", id=product.id)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, "Produto excluído com sucesso.")
        return redirect("lista_produto")

    return render(request, "catalog/product_detail.html", {
        "product" : product
    })