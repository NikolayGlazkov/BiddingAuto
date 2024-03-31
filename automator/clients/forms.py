from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Используйте все поля модели
        # Если нужны не все поля, можно перечислить их в списке, например: ['name', 'surname']
