from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reports/preview$', views.view,
        name='view'),
)
