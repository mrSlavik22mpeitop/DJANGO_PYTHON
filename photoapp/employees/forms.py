from django import forms
from .models import Employee
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
#DataFlair
class EmployeeCreate(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'second_name', 'email', 'phone', 'office_code', 'position')
        labels = {
                'first_name': ('Имя'),
                'second_name': ('Фамилия'),
                'email': ('Почта'),
                'phone': ('Телефон'),
                'office_code': ('Код сотрудника'),
                'position': ('Должность')
        }

        widgets = {
            'first_name' : TextInput(attrs={'maxlength':50}),
            'second_name': TextInput(attrs={'maxlength':50}),
            'email' : EmailInput(attrs={'type': 'email'}),
            'phone' : TextInput(attrs={'pattern': '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'}),
            'office_code' : NumberInput(attrs={'maxlength': 40}),
            'position' : TextInput(attrs={'maxlength': 50})
        }

