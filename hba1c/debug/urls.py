from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from . import views

urlpatterns = ()

if settings.DEBUG:
    urlpatterns += (
        url(r'^(?P<code>404|500)$', views.error),
        url(r'^storage/(?P<path>.*)$', serve, {
            'show_indexes': True,
            'document_root': settings.MEDIA_ROOT,
        })
    )
