from django.db import models
# from usuarios.models import Aluno, Responsavel

class Temperatura(models.Model):
    temperatura = models.CharField(
        max_length=50, verbose_name='Temperatura')

    class Meta:
        verbose_name = 'Temperatura'
        verbose_name_plural = 'Temperaturas'


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
    tempo = models.CharField(
        max_length=8, verbose_name='Tempo de Tratamento')
    grupo = models.CharField(
        max_length=8, verbose_name='Número do Grupo')
    temperatura = models.CharField(
        max_length=50, verbose_name='Temperatura')
#    responsavel = models.ForeignKey(
#        Responsavel, verbose_name='Nome do Responsável')

    class Meta:
        verbose_name = 'Tratamento de Material'
        verbose_name_plural = 'Tratamento de Materiais'

    def __str__(self):
        return self.grupo + ' - ' + self.tipo_material


class Grafico(models.Model):
    tratamento = models.ForeignKey(
        Tratamento, verbose_name='Tratamento')
    temperatura = models.ManyToManyField(
        Temperatura, related_name='temperatura_set')
