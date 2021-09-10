from django.shortcuts import render

from rest_framework import viewsets

from lesson_8.models import GameModel, GamerModel
from lesson_9.serializers import GameModelSerializer, GamerModelSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all()
    serializer_class = GameModelSerializer


class GamerViewSet(viewsets.ModelViewSet):
    queryset = GamerModel.objects.all()
    serializer_class = GamerModelSerializer






