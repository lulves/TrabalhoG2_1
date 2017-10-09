from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agendas.models import Agenda


class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class AgendaSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ('descricao', 'tipo')
