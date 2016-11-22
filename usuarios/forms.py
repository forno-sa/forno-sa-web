# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from usuarios.models import Usuario


class AuthenticationForm(forms.Form):
    matricula = forms.CharField(max_length=254)
    senha = forms.CharField(widget=forms.PasswordInput)


class CreateUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
    senha_again = forms.CharField(widget=forms.PasswordInput())

    # def clean(self):
    #     cleaned_data = super(CreateUsuarioForm, self).clean()
    #     senha = cleaned_data['senha']
    #     senha_again = cleaned_data['senha_again']

    #     if senha != senha_again:
    #        raise ValidationError("As senhas não são iguais")
    #     return cleaned_data

    # def save(self, commit=True):
    #     # import ipdb
    #     # ipdb.set_trace()
    #     user = User(username=self.data['nome_usuario'],
    #                 password=self.data['senha'],
    #                 first_name=self.data['nome'],
    #                 last_name=self.data['sobremone'],
    #                 email=self.data['email'],)
    #     user.save()
    #     # usuario = Usuario(user=user, nome=self.data['nome'],
    #     #                   sobrenome=self.data['sobrenome'],
    #     #                   matricula=self.data['matricula'],)
    #     # usuario.save()
    #     return user

    class Meta:
        model = Usuario
        fields = ['user', 'nome', 'sobrenome', 'matricula', 'email', 'senha',
                  'senha_again',]
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.TextInput(attrs={'class': 'form-control'}),
            'senha_again': forms.TextInput(attrs={'class': 'form-control'}),

        }


class UpdateUsuarioForm(CreateUsuarioForm):
    pass