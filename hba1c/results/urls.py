from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^reports/results$', views.view,
        name='view'),
    url(r'^reports/results/done$', views.done,
        name='done'),
    url(r'^reports/results/(?P<result_id>\d+)$', views.delete,
        name='delete'),
)
