from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ImageViewSet, AgentViewSet
from v1 import views


router = DefaultRouter()
router.register(r'image', ImageViewSet)
router.register(r'agent', AgentViewSet)

urlpatterns = [
    url(r'^image/(?P<image_id>[0-9a-f-]+)/file$', views.ImageFile.as_view()),
    url(r'^image/(?P<image_id>[0-9a-f-]+)/path$', views.ImagePath.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns.append(
    url(r'^', include(router.urls)),
)
