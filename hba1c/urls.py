from django.conf.urls import include, url

urlpatterns = (
    url(r'', include('hba1c.reports.urls',
        namespace='reports')),
    url(r'', include('hba1c.results.urls',
        namespace='results')),

    url(r'', include('hba1c.static.urls',
        namespace='static')),
    url(r'', include('hba1c.debug.urls')),
)
