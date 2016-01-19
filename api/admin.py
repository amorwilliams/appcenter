from django.contrib import admin

from api import models

# Register your models here.
admin.site.register(models.GameInfo)
admin.site.register(models.ServerInfo)
admin.site.register(models.ChannelInfo)
admin.site.register(models.SDKInfo)
admin.site.register(models.AppConfig)
