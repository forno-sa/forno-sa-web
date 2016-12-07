from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from tratamento.forms import CreateTratamentoForm
from tratamento.models import Tratamento, Grafico
from chartit import DataPool, Chart
from threading import Thread
from datetime import datetime, time, timedelta
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
        self.now = datetime.now().replace(microsecond=0)
        self.delta = timedelta(seconds=12)
        self.then = self.now + self.delta
        Thread.__init__(self)
        self.thread_numero = numero
        self.obj = obj
        self.valor = 0
        self.tempo = 0
        self.grafico_objeto = Grafico()

    def get_values(self):
        # self.write(b'i')
        # valor = ser.readline()
        # self.valor = float(valor[1:6])
        self.grafico_objeto.temperatura = self.valor
        self.grafico_objeto.tempo = self.now
        self.grafico_objeto.tratamento = self.obj
        self.grafico_objeto.save()
        while self.then < self.now + timedelta(minutes=10) or not\
              self.obj.finalizado:
            if self.now > self.then:
                # self.write(b'i')
                # valor = ser.readline()
                # self.valor = float(valor[1:6])
                self.grafico_objeto.temperatura = self.valor
                self.grafico_objeto.tempo = self.now
                self.grafico_objeto.tratamento = self.obj
                self.grafico_objeto.save()
                self.then = self.then + self.delta
            self.now = datetime.now().replace(microsecond=0)
        self.obj.finalizado = True
        self.obj.save()

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
    template_name = 'tratamentos/tratamento.html'
    form_class = CreateTratamentoForm

    def get_success_url(self):
        obj = self.get_context_data()['object']
        termopar = Termopar(1, obj)
        termopar.start()
        obj.timestamp = datetime.now().replace(microsecond=0)
        obj.save()
        return reverse('detail-tratamento', kwargs={'pk': obj.pk})

class DetailTratamentoView(ListView):
    model = Tratamento
    template_name = 'tratamentos/grafico.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        grafico = Grafico.objects.filter(
            tratamento=self.kwargs['pk']).values('temperatura', 'tempo')
        dados = []
        for obj in grafico:
            dados.append([obj['tempo'].__str__(),
                          obj['temperatura'].to_eng_string()])

        t = Tratamento.objects.get(pk=self.kwargs['pk'])

        kwargs['dados'] = dados
        kwargs['hora'] = t.tempo_tratamento.tempo.hour
        kwargs['min'] = t.tempo_tratamento.tempo.minute
        kwargs['seg'] = t.tempo_tratamento.tempo.second

        return kwargs
