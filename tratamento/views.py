from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, TemplateView, DetailView)
from tratamento.forms import CreateTratamentoForm
from tratamento.models import Tratamento, Grafico
from chartit import DataPool, Chart
from threading import Thread
from datetime import datetime, time, timedelta
from time import sleep
import serial
import random
import collections


class Termopar(Thread):
    def __init__(self, numero, obj, s):
        self.serial = s
        self.now = datetime.now().replace(microsecond=0)
        self.delta = timedelta(seconds=4)
        self.then = self.now + self.delta
        self.finish = self.now + timedelta(
            hours=obj.tempo_tratamento.tempo.hour,
            minutes=obj.tempo_tratamento.tempo.minute,
            seconds=obj.tempo_tratamento.tempo.second,)
        Thread.__init__(self)
        self.thread_numero = numero
        self.obj = obj
        self.valor = 0
        self.tempo = 0

    def get_values(self):
        self.serial.write(b'i1200')
        while self.then < self.finish or not self.obj.finalizado:
            dif = self.then - self.now
            if self.now > self.then:
                self.serial.write(b'v')
                valor = self.serial.readline()
                self.valor = float(valor)
                grafico_objeto = Grafico()
                grafico_objeto.temperatura = self.valor
                grafico_objeto.tempo = self.now
                grafico_objeto.tratamento = self.obj
                grafico_objeto.save()
                self.then = self.now + self.delta
            sleep(dif.total_seconds()+1)
            self.now = datetime.now().replace(microsecond=0)
        self.obj.finalizado = True
        self.obj.save()

    def close(self):
        self.serial.close()
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
        try:
            s = serial.Serial('/dev/ttyACM0', 9600)
            termopar = Termopar(1, obj, s)
            termopar.start()
        except serial.SerialException:
            # TODO: Redirecionar para uma tela de erros ou senão enviar uma
            # mensagem para o form dizendo que não há forno conectado.
            # raise ValueError("O forno não está conectado!")
            pass
        obj.timestamp = datetime.now().replace(microsecond=0)
        obj.save()
        return reverse('detail-tratamento', kwargs={'pk': obj.pk})

class DetailTratamentoView(UpdateView):
    model = Tratamento
    template_name = 'tratamentos/grafico.html'

    def post(self, request, *args, **kwargs):
        pass

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
        if not t.finalizado:
            inicio = t.timestamp
            fim = inicio + timedelta(
                hours=t.tempo_tratamento.tempo.hour,
                minutes=t.tempo_tratamento.tempo.minute,
                seconds=t.tempo_tratamento.tempo.second,)
            agora = datetime.now()
            restante = (fim-inicio) - (agora-inicio)
            kwargs['seg_total'] = int(restante.total_seconds())
        else:
            kwargs['seg_total'] = 0

        
        kwargs['tratamento'] = t 
        kwargs['dados'] = dados

        return kwargs
