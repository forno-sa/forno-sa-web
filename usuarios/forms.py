# -*- coding: utf-8 -*-
from django import forms

class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)