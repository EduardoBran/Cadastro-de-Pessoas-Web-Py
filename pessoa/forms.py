from django import forms
from django.forms import fields, models

from .models import Pessoa


class PessoaForm(forms.ModelForm):
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
