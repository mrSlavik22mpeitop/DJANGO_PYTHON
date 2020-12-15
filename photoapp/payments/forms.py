from django import forms
from .models import Payment
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
#DataFlair
class PaymentCreate(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('customers_id', 'products_id', 'payment_Date', 'amount')
        labels = {
            'customers_id': ('Имя покупателя'),
            'products_id': ('Название товара'),
            'payment_Date': ('Дата покупки'),
            'amount': ('Количество')
        }

        widgets = {
            'payment_Date': forms.DateInput(attrs={'type': 'date'})
        }