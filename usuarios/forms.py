# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from usuarios.models import Usuario


class AuthenticationForm(forms.Form):
    matricula = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUsuarioForm(forms.ModelForm):
    nome = forms.CharField(max_length=50)
    sobrenome = forms.CharField(max_length=50)
    matricula = forms.CharField(max_length=10)
    email = forms.EmailField()
    senha = forms.CharField(min_length=6, max_length=16)
    senha_again = forms.CharField(min_length=6, max_length=16)

    def clean_senha_again(self):
        cleaned_data = super(CreateUsuarioForm, self).clean()
        senha = cleaned_data['senha']
        senha_again = cleaned_data['senha_again']

        if senha != senha_again:
           raise ValidationError("As senhas não são iguais")
        return cleaned_data


    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'matricula', 'email', 'senha',
                  'senha_again',]


class UpdateUsuarioForm(CreateUsuarioForm):
    pass