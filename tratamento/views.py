from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from tratamento.forms import CreateTratamentoForm
from tratamento.models import Tratamento, Grafico
from chartit import DataPool, Chart
from threading import Thread
from datetime import datetime, time
import serial
import random
import collections


class Termopar(Thread):
    def __init__(self, numero, obj):
        try:
            self.serial = serial.Serial('/dev/ttyACM0', 9600)
        except serial.SerialException:
            # TODO: Redirecionar para uma tela de erros ou senão enviar uma
            # mensagem para o form dizendo que não há forno conectado.
            # raise ValueError("O forno não está conectado!")
            pass
        Thread.__init__(self)
        self.thread_numero = numero
        self.obj = obj
        self.valor = 0
        self.tempo = 0

    def get_values(self):
        # self.write(b'i')
        # valor = ser.readline()
        # self.valor = float(valor[1:6])
        self.valor = round(random.uniform(0,300), 2)
        if self.tempo == 20:
            self.obj.finalizado = True
            self.obj.save()
        self.tempo += 5

    def close(self):
        # self.serial.close()
        pass

    def run(self):
        while not self.obj.finalizado:
            self.get_values()
            print('Temperatura: %s' % self.valor)
        self.close()

class CreateTratamentoView(CreateView):
    model = Tratamento
    template_name = 'tratamento.html'
    form_class = CreateTratamentoForm

    def get_success_url(self):
        obj = self.get_context_data()['object']
        termopar = Termopar(1, obj)
        termopar.start()
        obj.timestamp = datetime.now()
        obj.save()
        return reverse('detail-tratamento', kwargs={'pk': obj.pk})

class DetailTratamentoView(ListView):
    model = Tratamento
    template_name = 'grafico.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self

        grafico = Grafico.objects.values('temperatura', 'tempo')
        dados = {}
        for obj in grafico:
            dados[obj['tempo'].__str__()] = obj['temperatura'].to_eng_string()

        kwargs['dados'] = dados

        return kwargs
