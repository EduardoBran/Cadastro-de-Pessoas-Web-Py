from django.contrib import admin

from .models import Pessoa


# editando a ação
@admin.action(description='Ativar todas as Pessoas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)

@admin.action(description='Desativar todas as Pessoas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'sobrenome',
        'data_nascimento',
        'ativo'
    ]
    
    list_filter = [
        'ativo',
        'data_nascimento'
    ]
    
    search_fields = [
        'nome'
    ]

    actions = [
        ativar_todos,
        desativar_todos
    ]

admin.site.register(Pessoa, PessoaAdmin)
