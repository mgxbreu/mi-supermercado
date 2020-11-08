from django import forms
from slist.models import Product, Supermarket


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product',)


class SupermarketForm(forms.ModelForm):
    class Meta:
        model = Supermarket
        fields = ('supermarket',)
