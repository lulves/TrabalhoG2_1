from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agendas.models import *


class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class AgendaSerializer (serializers.HyperlinkedModelSerializer):
    usuarios = UserSerializer(many=False)
    participantes = UserSerializer(many=True)
    class Meta:
        model = Agenda
        fields = ('descricao', 'tipo')

class ConviteSerializer (serializers.HyperlinkedModelSerializer):
    realizador = UserSerializer(many = False)
    compromisso = UserSerializer (many = False)
    convidado = UserSerializer (many = False)
    class Meta:
        model = Convite
        fields = ('realizador', 'compromisso', 'convidado', 'resposta')
