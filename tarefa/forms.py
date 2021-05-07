from django import forms
from .models import TarefaBd

class ConteudoForm(forms.ModelForm):
    class Meta:
        model=TarefaBd
        fields=('conteudo',)