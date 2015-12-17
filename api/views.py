from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, generics, views, mixins
from rest_framework.decorators import detail_route

from api.models import *
from api.serializers import *


class GameInfoViewSet(viewsets.ModelViewSet):
    queryset = GameInfo.objects.all()
    serializer_class = GameInfoSerializer

class ServerInfoViewSet(viewsets.ModelViewSet):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer

class ChannelInfoViewSet(viewsets.ModelViewSet):
    queryset = ChannelInfo.objects.all()
    serializer_class = ChannelInfoSerializer

class SDKInfoViewSet(viewsets.ModelViewSet):
    queryset = SDKInfo.objects.all()
    serializer_class = SDKInfoSerializer


class AppConfigDetailViewSet(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    queryset = AppConfig.objects.all()
    serializer_class = AppConfigSerializer
    lookup_field = 'pkg_id'

class AppConfigListViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = AppConfig.objects.all()
    serializer_class = AppConfigCreateSerializer
