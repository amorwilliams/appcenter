from __future__ import unicode_literals

import uuid

from django.db import models

SERVER_STATUS = (
    (1, 'Normal'),
    (2, 'Busy'),
    (3, 'Full'),
    (0, 'Stop'),
    (-1, 'Hide'),
)

WHITE_LIST = (
    (0, 'Clear'),
    (1, 'White'),
    (2, 'Black'),
)

class GameInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    version = models.CharField(max_length=50, blank=True, default='1.0.0')
    announcement = models.TextField(blank=True)
    activity_pic1 = models.ImageField(upload_to='img/', blank=True)
    activity_pic2 = models.ImageField(upload_to='img/', blank=True)
    activity_pic3 = models.ImageField(upload_to='img/', blank=True)

    def __unicode__(self):
        return self.name

class GroupInfo(models.Model):
    name = models.CharField(max_length=50, blank=False)
    game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE, related_name='groups')
    status = models.IntegerField(choices=SERVER_STATUS, default=0)
    index = models.IntegerField(default=1)
    isnew = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class ServerInfo(models.Model):
    name = models.CharField(max_length=50, blank=False)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    status = models.IntegerField(choices=SERVER_STATUS, default=0)
    index = models.IntegerField(default=1)
    timeout = models.IntegerField(default=10)
    isnew = models.BooleanField(default=True)
    game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE, related_name='servers')
    group_id = models.ForeignKey(GroupInfo, blank=True, related_name='servers')

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


class Whitelist(models.Model):
    ip = models.GenericIPAddressField(db_index=True, unique=True)
    status = models.IntegerField(choices=WHITE_LIST, default=0)

    def __unicode__(self):
        return "[{ip}]-[{status}]".format(ip=self.ip, status=WHITE_LIST[self.status][1])
