from django.db import models

class Sale(models.Model):
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado')
    ]

    data = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    def __str__(self):
        return f'{self.id}' - f'{self.status}'

class SaleItem(models.Model):

    produto = models.CharField(max_length=100, unique=True, null=False)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.produto}'
