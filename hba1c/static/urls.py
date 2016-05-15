from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.landing,
        name='landing'),

    url(r'^terms$', views.terms,
        name='terms'),
    url(r'^privacy$', views.privacy,
        name='privacy'),

    url(r'^sitemap.xml$', views.sitemap,
        name='sitemap'),
)
