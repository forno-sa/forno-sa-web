# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from usuarios.models import Usuario


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Matrícula", max_length=10,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Matrícula',
                   'name': 'matricula'}))
    password = forms.CharField(
        label="Senha", max_length=50,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Senha',
                   'name': 'password'}))


class CreateUsuarioForm(forms.ModelForm):
    nome = forms.CharField(max_length=50)
    sobrenome = forms.CharField(max_length=50)
    matricula = forms.CharField(max_length=10)
    email = forms.EmailField()
    senha = forms.CharField(min_length=6, max_length=16)
    senha_again = forms.CharField(min_length=6, max_length=16)

    def clean_matricula(self):
        cleaned_data = super(CreateUsuarioForm, self).clean()
        matricula = cleaned_data['matricula']
        if Usuario.objects.filter(matricula=matricula).exists():
            raise ValidationError("Um usuário com essa matrícula já existe")
        return matricula

    def clean_senha_again(self):
        cleaned_data = super(CreateUsuarioForm, self).clean()
        senha = cleaned_data['senha']
        senha_again = cleaned_data['senha_again']

        if senha != senha_again:
           raise ValidationError("As senhas não são iguais")
        return senha_again

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'matricula', 'email', 'senha',
                  'senha_again',]


class UpdateUsuarioForm(forms.ModelForm):
    nome = forms.CharField(max_length=50)
    sobrenome = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email']