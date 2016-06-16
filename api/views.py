from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, generics, views, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from api.models import *
from api.serializers import *


class GameInfoViewSet(viewsets.ModelViewSet):
    queryset = GameInfo.objects.all()
    serializer_class = GameInfoSerializer

class GroupInfoViewSet(viewsets.ModelViewSet):
    queryset = GroupInfo.objects.all()
    serializer_class = GroupInfoFullSerializer

class ServerInfoViewSet(viewsets.ModelViewSet):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer

class ChannelInfoViewSet(viewsets.ModelViewSet):
    queryset = ChannelInfo.objects.all()
    serializer_class = ChannelInfoSerializer

class SDKInfoViewSet(viewsets.ModelViewSet):
    queryset = SDKInfo.objects.all()
    serializer_class = SDKInfoSerializer


class AppConfigViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset = AppConfig.objects.all()
        serializer = AppConfigSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = AppConfig.objects.all()
        config = get_object_or_404(queryset, pkg_id=pk)

        serializer = AppConfigSerializer(config)
        print type(serializer.data['game']['servers'])

        remote_ip = self.getIPFromDJangoRequest(request)
        print remote_ip

        white_ip = Whitelist.objects.get(ip=remote_ip)
        if white_ip.status == 2:
            serializer.data['game']['servers'] = []
        elif white_ip.status == 1:
            for server in serializer.data['game']['servers']:
                if server['status'] < 1:
                    server['status'] = 1

        return Response(serializer.data)

    def getIPFromDJangoRequest(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            return request.META['HTTP_X_FORWARDED_FOR']
        else:
            return request.META['REMOTE_ADDR']
