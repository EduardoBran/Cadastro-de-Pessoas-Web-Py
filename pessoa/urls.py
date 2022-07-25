from django.urls import path

from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView

urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo'),
    path('<int:pk>/editar', PessoaUpdateView.as_view(), name='pessoa.editar'),
]

