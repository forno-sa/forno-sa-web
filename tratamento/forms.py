# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from tratamento.models import Temperatura, Tempo, Tratamento
from datetime import time


class CreateTratamentoForm(forms.ModelForm):
    tipo_material = forms.CharField(max_length=50)
    tempo_tratamento = forms.CharField()
    temperatura_tratamento = forms.DecimalField()
    grupo = forms.CharField(max_length=8)

    def clean_temperatura_tratamento(self):
        temperatura = self.cleaned_data['temperatura_tratamento']
        if temperatura > 1200:
            raise forms.ValidationError("A temperatura tem que ser menor que 1200º")
        return temperatura

    def clean(self):
        temperatura = self.cleaned_data['temperatura_tratamento']
        tempo = self.cleaned_data['tempo_tratamento']

        temperatura_ajustada = Temperatura.objects.get_or_create(
            temperatura=temperatura)
        self.cleaned_data['temperatura_tratamento'] = temperatura_ajustada[0]

        tempo_list = tempo.split(':')
        if len(tempo_list) == 3:
            tempo = time(
                hour=int(tempo_list[0]), minute=int(tempo_list[1]),
                second=int(tempo_list[2]),)
        elif len(tempo_list) == 2:
            tempo = time(
                hour=int(tempo_list[0]), minute=int(tempo_list[1]),)
        elif len(tempo_list) == 1:
            tempo = time(hour=int(tempo_list[0]),)

        tempo_ajustado = Tempo.objects.get_or_create(tempo=tempo)
        self.cleaned_data['tempo_tratamento'] = tempo_ajustado[0]

        return self.cleaned_data

    

    class Meta:
        model = Tratamento
        fields = ['tipo_material', 'temperatura_tratamento',
                  'tempo_tratamento', 'grupo',]
