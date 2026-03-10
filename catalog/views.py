from datetime import date 
from django.contrib import messages
from django.shortcuts import render, redirect
from catalog.forms import ProdutoForm
from catalog.models import Categoria, Produto
from sales.models import Sale, SaleItem
from django.db.models import Sum


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


def dashboard(request):
    total_products = Produto.objects.count()

    total_categories = Produto.objects.count()
    active_products = Produto.objects.filter(status=True).count()
    inactive_products = Produto.objects.filter(status=False).count()

    total_revenue = Sale.objects.filter(status='pago').aggregate(Sum('total'))

    context = {
        'total_products' : total_products,
        'total_categories' : total_categories,
        'active_products' : active_products,
        'inactive_products' : inactive_products
    }
    
    return render(request, 'dashboard/dashboard.html', context)

def vendas_dashboard(request):
    today_sales = Sale.objects.filter(data=date.today()).count

    contexto = {
        "today_sales" : today_sales
    }

    return render(request, 'dashboard/dashboard.html', contexto)


def criar_produto(request):
        if request.method == "POST":
            form = ProdutoForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Produto criado com sucesso.")
                return redirect("produto")
            
            else:
                messages.error(request, "Erro ao criar o produto. Verifique os dados.")
        
        else:
            form = ProdutoForm()

        products = Produto.objects.all()
        return render(request, "catalog/pessoa_form.html", {"form" : form})


def editar_produto(request, id):
    product = Produto.objects.get(id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("produto")
        
    else:
        form = ProdutoForm(instance=product)

    products = Produto.objects.all()

    return render(request, "catalog/pessoa_form.html", {
        "form" : form,
        "product" : product
    })


def excluir_produto(request, id):
    product = Produto.objects.get(id=id)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, "Produto excluído com sucesso.")
        return redirect("produto")

    return render(request, "catalog/pessoa_confirm_delete.html", {
        "product" : product
    })