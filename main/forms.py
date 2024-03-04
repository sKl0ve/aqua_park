from .models import Tickets
from django.forms import ModelForm, TextInput

class TicketsForm(ModelForm):
    class Meta:
        model = Tickets
        fields = ['name', 'number', 'email', 'qnt']
        
        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'ФИО'
            }),
            "number": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Номер телефона'
            }),
            "email": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Электронная почта'
            }),
            "qnt": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Количество билетов'
            }),
        }