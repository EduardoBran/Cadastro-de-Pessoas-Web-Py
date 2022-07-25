from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import PessoaForm
from .models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome')
    template_name = 'pessoa/pessoa_lista.html'
    context_object_name = 'pessoas'
    

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'
    

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'
