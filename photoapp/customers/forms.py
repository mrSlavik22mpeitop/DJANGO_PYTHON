from django import forms
from .models import Customer
from django.forms import ModelForm, TextInput, EmailInput
#DataFlair
class CustomerCreate(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('employees_id', 'products_id','first_name', 'second_name', 'email','phone','location','postal_Code')
        labels = {
                'employees_id': ('Имя сотрудника'),
                'products_id': ('Название товара'),
                'first_name': ('Имя'),
                'second_name': ('Фамилия'),
                'email': ('Почта'),
                'phone': ('Телефон'),
                'location': ('Город'),
                'postal_Code': ('Почтовый индекс')
        }
        widgets = {
            'first_name' : TextInput(attrs={'maxlength': 50}),
            'second_name' : TextInput(attrs={'maxlength': 50}),
            'email' : EmailInput(attrs={'type': 'email'}),
            'phone' : TextInput(attrs={'pattern': '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'}),
            'location' : TextInput(attrs={'maxlength': 50}),
            'postal_code': TextInput(attrs={'maxlength': 40})
        }