from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('hba1c.reports.reports_preview.urls',
        namespace='preview')),

    url(r'^create$', views.create,
        name='create'),
    url(r'^reports/name$', views.name,
        name='name'),
    url(r'^reports/generating$', views.generate,
        name='generate'),
    url(r'^reports/download$', views.download,
        name='download'),
)
