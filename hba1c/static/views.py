from django.shortcuts import render

from hba1c.session.enums import StageEnum
from hba1c.session.decorators import funnel_stage

@funnel_stage(StageEnum.LANDING)
def landing(request, session):
    return render(request, 'static/landing.html', {
        'session': session,
    })

def terms(request):
    return render(request, 'static/terms.html')

def privacy(request):
    return render(request, 'static/privacy.html')

def sitemap(request):
    return render(request, 'static/sitemap.xml', {
        'urls': (
            'static:landing',
            'static:faq',
        ),
    })
