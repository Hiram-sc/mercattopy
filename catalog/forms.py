from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Produto

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'status', 'categoria']
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome.split()) < 2:
            raise ValidationError(
                'Informe o nome completo. Nome e sobrenome.'
            )
        return nome
    
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 0:
            raise ValidationError(
                'O preço não pode ser negativo.'
            )
        return preco
    
    def clean_quantidade_estoque(self):
        estoque = self.cleaned_data.get('quantidade_estoque')
        if estoque < 0:
            raise ValidationError(
                'O estoque não pode ser negativo.'
            )
        return estoque
    
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria.status:
            raise ValidationError(
                'A categoria selecionada não está ativa.'
            )
        return categoria
