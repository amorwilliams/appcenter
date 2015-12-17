from __future__ import unicode_literals

import uuid

from django.db import models

SERVER_STATUS = (
    ('N', 'Normal'),
    ('B', 'Busy'),
    ('F', 'Full'),
    ('S', 'Stop'),
)

class GameInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    version = models.CharField(max_length=50, blank=True, default='1.0.0')

    def __unicode__(self):
        return self.name

class ServerInfo(models.Model):
    name = models.CharField(max_length=50, blank=False)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    status = models.CharField(max_length=1, choices=SERVER_STATUS, default='N')
    new = models.BooleanField(default=True)
    game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE, related_name='servers')

    def __unicode__(self):
        return self.name


class ChannelInfo(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.name


class SDKInfo(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.name


class AppConfig(models.Model):
    pkg_id = models.UUIDField(unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, blank=True)
    game = models.ForeignKey(GameInfo, on_delete=models.CASCADE, related_name='configs')
    channel = models.ForeignKey(ChannelInfo, on_delete=models.CASCADE, related_name='configs')
    sdk = models.ForeignKey(SDKInfo, on_delete=models.CASCADE, related_name='configs')

    def __unicode__(self):
        return self.pkg_id
