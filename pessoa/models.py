from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=50)
    link_git = models.URLField(max_length=150, null=True, blank=True)
    ativo = models.BooleanField(default=True)
