# -*- coding: utf-8 -*-
from django import forms
from usuarios.models import Usuario


class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUsuarioForm(forms.ModelForm):
    nome = forms.CharField(max_length=50)
    sobrenome = forms.CharField(max_length=50)
    matrícula = forms.CharField(min_length=9, max_length=10)
    email = forms.EmailField()
    senha = forms.CharField(min_length=6, max_length=16)
    senha_again = forms.CharField(min_length=6, max_length=16)

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'matricula', 'email', 'senha',
                  'senha_again']


class UpdateUsuarioForm(CreateUsuarioForm):
    pass