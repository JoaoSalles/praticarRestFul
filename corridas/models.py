# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Motorista(models.Model):
    nome = models.CharField(max_length=125)
    data_nascimento = models.DateField()
    cpf = models.BigIntegerField(unique=True)
    modelo = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    sexo = models.CharField(max_length=1, default="M")


    def __unicode__(self):
        return u"Nome: %s, CPF: %s" % (self.nome,self.cpf)


class Passageiro(models.Model):
    nome = models.CharField(max_length=125)
    data_nascimento = models.DateField()
    cpf = models.BigIntegerField(unique=True)
    sexo = models.CharField(max_length=1, default="M")

    def __unicode__(self):
        return u"Nome: %s, CPF: %s" % (self.nome,self.cpf)


class Corrida(models.Model):
    valor = models.FloatField()
    passageiro = models.ForeignKey(Passageiro)
    motorista = models.ForeignKey(Motorista)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Passageiro: %s, Motorista: %s" % (self.passageiro,self.motorista)

