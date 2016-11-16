from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, TemplateView


class CreateTratamentoView(TemplateView):
    template_name = 'tratamento.html'

