from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Agenda(models.Model):
	descricao = models.CharField(max_length= 300, null= True, blank=False)
	usuario = models.ForeignKey(User)
	visivel = models.BooleanField ("Visivel")
	tipo = models.CharField(max_length= 200, null= True, blank=False)
	institucional= models.BooleanField("Institucional")
	participantes = models.ManyToManyField(User, related_name='item_participantes')
	def __str__ (self):
		return '{}'.format(self.tipo)

class Compromisso(models.Model):
	nome = models.CharField(max_length=150)
	dataI = models.DateTimeField(blank=True, null=True)
	dataF = models.DateTimeField(blank=True, null=True)
	agendas = models.ForeignKey(Agenda, related_name='agendas', blank = True)
	convidado = models.ManyToManyField(User, related_name='Convidados')
	def __str__ (self):
		return '{}'.format(self.nome)

class Convite (models.Model):
        realizador = models.ForeignKey(User, null=True, blank=False, related_name="Sender")
        convidado = models.ForeignKey(User, null=True, blank=False, related_name="Receiver")
        compromisso = models.ForeignKey(Compromisso, null=True, blank=False, related_name="Compromisso")
        resposta = models.BooleanField(default=False, verbose_name="Aceito")
