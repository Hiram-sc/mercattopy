from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome}'
    
class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True) 
    preco = models.DecimalField(max_digits=6 ,decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    
    def __str__(self):
        return f'{self.nome}'