from django import forms
from .models import Order
from django.forms import ModelForm, DateInput, TextInput
#DataFlair
class OrderCreate(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customers_id', 'order_date', 'required_date', 'shipped_date', 'status')
        labels = {
                'customers_id': ('Имя покупателя'),
                'order_date': ('Дата заказа'),
                'required_date': ('Дата получения'),
                'shipped_date': ('Дата отправки'),
                'status': ('Статус отправки'),
        }
        widgets = {
            'status': TextInput(attrs={'maxlength' : 50}),
            'required_date': forms.DateInput(attrs={'type' : 'date'}),
            'shipped_date': forms.DateInput(attrs={'type' : 'date'}),
            'order_date': forms.DateInput(attrs={'type' : 'date'})
        }
