from django.contrib import messages
from django.shortcuts import render, redirect
from sales.models import Sale, SaleItem
from catalog.models import Produto

def registrar_venda(request):
    produtos = Produto.objects.all()
    
    if request.method == 'POST':
        sale = Sale.objects.create()
        total = 0

        for produto in produtos:
            quantidade = int(request.POST.get(f"quantidade_{produto.id}", 0))

            if quantidade > 0:
                if quantidade > produto.quantidade_estoque:
                    messages.error(request, f'Estoque insuficiente para {produto.nome}')
                    return render(request, "sales/register_sale.html", {"produtos" : produtos})
                
                subtotal = produto.preco * quantidade
                total += subtotal

            messages.success(request, 'Venda registrada com sucesso.')
            return redirect("vendas")
    
    return render(request, "sales/register_sale.html", {"produtos" : produtos})
