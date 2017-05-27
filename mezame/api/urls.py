from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^image/$', views.ImageList.as_view()),
    url(r'^image/(?P<image_id>[0-9a-f-]+)$', views.ImageDetail.as_view()),
    url(r'^image/(?P<image_id>[0-9a-f-]+)/file$', views.ImageFile.as_view()),
    url(r'^image/(?P<image_id>[0-9a-f-]+)/path$', views.ImagePath.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
