from django.shortcuts import render
from django.views.generic import ListView

from .models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome')
    template_name = 'pessoa/pessoa_lista.html'
    

