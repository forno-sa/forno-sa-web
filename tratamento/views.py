from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, TemplateView
from tratamento.forms import CreateTratamentoForm
from tratamento.models import Tratamento


class CreateTratamentoView(CreateView):
    model = Tratamento
    template_name = 'tratamento.html'
    form_class = CreateTratamentoForm


class DetailTratamentoView(TemplateView):
    model = Tratamento
    template_name = 'grafico.html'

