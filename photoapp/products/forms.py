from django import forms
from .models import Product
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
#DataFlair
class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_company', 'price', 'rating')
        labels = {
                'product_name': ('Имя товара'),
                'product_company': ('Бренд'),
                'price': ('Стоимость'),
                'rating': ('Оценка')
        }

        widgets = {
            'product_name' : TextInput(attrs={'maxlength': 50}),
            'product_company' : TextInput(attrs={'maxlength': 50}),
            'price' : NumberInput(attrs={'maxlength': 40}),
            'rating' : NumberInput(attrs={'maxlength': 50})
        }
