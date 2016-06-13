from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'games', views.GameInfoViewSet)
router.register(r'servers', views.ServerInfoViewSet)
router.register(r'groups', views.GroupInfoViewSet)
router.register(r'channels', views.ChannelInfoViewSet)
router.register(r'sdks', views.SDKInfoViewSet)
router.register(r'configs', views.AppConfigDetailViewSet)
router.register(r'configs', views.AppConfigListViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
