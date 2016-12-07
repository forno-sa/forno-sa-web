from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Nome de usuário')
    nome = models.CharField(
        max_length=50, verbose_name='Nome')
    sobrenome = models.CharField(
        max_length=50, verbose_name='Sobrenome')
    email = models.EmailField()
    data_criacao = models.DateField(
        default=timezone.now, verbose_name='Data de cadastro')
    matricula = models.CharField(
        max_length=10, verbose_name='Matrícula', unique=True)
    #TODO: Retirar esse campo, senha é salva no user
    senha = models.CharField(
        max_length=100, verbose_name='Senha')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome