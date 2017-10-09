from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from agendas.models import *
from agendas.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

# Create your views here.
