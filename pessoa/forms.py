from django import forms
from django.forms import fields, models

from .models import Pessoa


class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'sobrenome',
            'data_nascimento',
            'email',
            'link_git',
            'ativo'
            ]
