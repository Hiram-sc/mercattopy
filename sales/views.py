from django.shortcuts import render
from sales.models import Sale, SaleItem
from catalog.models import Produto

def registrar_venda(request):
    produtos = Produto.objects.all()
    
    return render(request, "sales/register_sale.html", {"produtos" : produtos})
