from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin


# class UsuarioManager(BaseUserManager):
#     def create_user(self, *args, **kwargs):
#         matricula = kwargs["matricula"]
#         password = kwargs["senha"]
#         kwargs.pop("senha")
#         user = self.model(**kwargs)
#         user.set_password(password)
#         user.is_staff=True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, *args, **kwargs):
#         user = self.create_user(**kwargs)
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

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
    # XXX min_length is set in the forms, not here
    matricula = models.CharField(
        max_length=10, verbose_name='Matrícula', unique=True)
    senha = models.CharField(
        max_length=100, verbose_name='Senha')

    # USERNAME_FIELD = 'matricula'
    # objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome