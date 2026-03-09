from django.shortcuts import render
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
                    return render(request, "sales/register_sale.html", {"produtos" : produtos})
                
                subtotal = produto.preco * quantidade
                total += subtotal
    
    return render(request, "sales/register_sale.html", {"produtos" : produtos})
