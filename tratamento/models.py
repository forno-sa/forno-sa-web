from django.db import models
# from usuarios.models import Aluno, Responsavel


class TipoMaterial(models.Model):
    pass


class Material(models.Model):
    tipo_material = models.ForeignKey(
        TipoMaterial, verbose_name='Tipo de Material')


class Tratamento(models.Model):
    # tipo_material = models.ForeignKey(
    #     TipoMaterial, verbose_name='Tipo do Material')
    tipo_material = models.CharField(
        max_length=50, verbose_name='Tipo do Material')
    tempo = models.CharField(
        max_length=8, verbose_name='Tempo de Tratamento')
    grupo = models.CharField(
        max_length=8, verbose_name='Número do Grupo')
#    responsavel = models.ForeignKey(
#        Responsavel, verbose_name='Nome do Responsável')

