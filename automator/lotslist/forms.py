from django import forms
from .models import LotListBank

class LotForm(forms.ModelForm):
    class Meta:
        model = LotListBank
        fields = '__all__'  # Используйте все поля модели
        exclude = ('client',)

    def __init__(self, *args, **kwargs):
        self.client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        if self.client:
            self.fields['client'].initial = self.client