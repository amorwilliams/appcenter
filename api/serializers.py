from rest_framework import serializers

from api.models import *


class ServerInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('name', 'ip', 'port', 'status', 'index', 'timeout', 'isnew', 'game_id')


class ServerInfoFullSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('name', 'ip', 'port', 'status', 'index', 'timeout', 'isnew')


class GameInfoSerializer(serializers.HyperlinkedModelSerializer):
    # servers = ServerInfoSerializer(many=True)

    class Meta:
        model = GameInfo
        fields = ('name', 'version', 'servers')


class GameInfoFullSerializer(serializers.HyperlinkedModelSerializer):
    servers = ServerInfoFullSerializer(many=True)

    class Meta:
        model = GameInfo
        fields = ('name', 'version', 'servers')


class ChannelInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChannelInfo
        fields = ('name',)


class SDKInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SDKInfo
        fields = ('name',)


class AppConfigCreateSerializer(serializers.HyperlinkedModelSerializer):
    pkg_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = AppConfig
        fields = ('pkg_id', 'name', 'game', 'channel', 'sdk')


class AppConfigSerializer(serializers.HyperlinkedModelSerializer):
    pkg_id = serializers.UUIDField(read_only=True)
    game = GameInfoFullSerializer(read_only=True)
    channel = ChannelInfoSerializer(read_only=True)
    sdk = SDKInfoSerializer(read_only=True)

    class Meta:
        model = AppConfig
        fields = ('pkg_id', 'name', 'game', 'channel', 'sdk')
