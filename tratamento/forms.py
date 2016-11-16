# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from tratamento.models import Tratamento


class CreateTratamentoForm(forms.ModelForm):
    tipo_material = forms.CharField(max_length=50)
    tempo = forms.CharField(max_length=8)
    grupo = forms.CharField(max_length=8)

    class Meta:
        model = Tratamento
        fields = ['tipo_material', 'tempo', 'grupo',]
