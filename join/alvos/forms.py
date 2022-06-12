from django import forms
from .models import Alvo


class AlvosForm(forms.ModelForm):

    class Meta:
        model = Alvo
        fields = '__all__'

        labels = {'data_expiracao': 'Data de Expiração'}
