from django.db import models
# from usuarios.models import Aluno, Responsavel


class Temperatura(models.Model):
    temperatura = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Temperatura')

    class Meta:
        verbose_name = 'Temperatura'
        verbose_name_plural = 'Temperaturas'

    def __str__(self):
        return '%s ºC' % self.temperatura


class Tempo(models.Model):
    tempo = models.TimeField(verbose_name='Temperatura')

    class Meta:
        verbose_name = 'Tempo'
        verbose_name_plural = 'Tempos'

    def __str__(self):
        return '%s:%s:%s' % (self.tempo.hour, self.tempo.minute,
                             self.tempo.second)


class TipoMaterial(models.Model):
    pass

    class Meta:
        verbose_name = 'Tipo de Material'
        verbose_name_plural = 'Tipo de Materiais'


class Material(models.Model):
    tipo_material = models.ForeignKey(
        TipoMaterial, verbose_name='Tipo de Material')

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'


class Tratamento(models.Model):
    # tipo_material = models.ForeignKey(
    #     TipoMaterial, verbose_name='Tipo do Material')
    tipo_material = models.CharField(
        max_length=50, verbose_name='Tipo do Material')
    grupo = models.CharField(
        max_length=8, verbose_name='Número do Grupo')

    tempo_tratamento = models.ForeignKey(
        Tempo, verbose_name='Tempo de Tratamento')
    temperatura_tratamento = models.ForeignKey(
        Temperatura, verbose_name='Temperatura Máxima')
    # responsavel = models.ForeignKey(
    #     Responsavel, verbose_name='Nome do Responsável')
    finalizado = models.BooleanField(
        default=False, verbose_name='Processo Finalizado')
    timestamp = models.DateField(
        null=True, blank=True, verbose_name='Hora de Início do Tratamento')

    class Meta:
        verbose_name = 'Tratamento de Material'
        verbose_name_plural = 'Tratamento de Materiais'

    def __str__(self):
        return self.grupo + ' - ' + self.tipo_material

class Grafico(models.Model):
    tratamento = models.ForeignKey(
        Tratamento, verbose_name='Tratamento')
    temperatura = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Temperatura')
    tempo = models.TimeField(verbose_name='Temperatura')

    class meta:
        verbose_name = 'Gráfico'
        verbose_name_plural = 'Gráficos'

    def __str__(self):
        return 'Gráfico do Tratamento %s' % self.tratamento.pk
