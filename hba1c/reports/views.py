from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.cache import never_cache

from hba1c.utils.ajax import ajax
from hba1c.session.enums import StageEnum
from hba1c.session.decorators import funnel_stage

from hba1c.session.models import Session

from .forms import NameForm

@funnel_stage(StageEnum.LANDING)
def create(request, session):
    return redirect(StageEnum.urlconf(StageEnum.NAME))

@funnel_stage(StageEnum.NAME)
def name(request, session):
    if request.method == 'POST':
        form = NameForm(request.POST, instance=session)

        if form.is_valid():
            form.save()

            return Session.objects.set_and_redirect(request, StageEnum.RESULTS)
    else:
        form = NameForm(instance=session)

    return render(request, 'reports/name.html', {
        'form': form,
    })

@ensure_csrf_cookie
@never_cache
@ajax(required=False)
@funnel_stage(StageEnum.GENERATE)
def generate(request, session):
    if not session.generating_pdf:
        response = Session.objects.set_and_redirect(request, StageEnum.PREVIEW)

        if request.is_ajax():
            return {'redirect': response['Location']}

        return response

    if request.is_ajax():
        return {}

    return render(request, 'reports/generating.html', {
        'session': session,
    })

@funnel_stage(StageEnum.PREVIEW, fallback=StageEnum.urlconf(StageEnum.RESULTS))
def preview(request, session):
    if request.method == 'POST':
        return Session.objects.set_and_redirect(request, StageEnum.DOWNLOAD)

    return render(request, 'reports/preview.html', {
        'session': session,
    })

@never_cache
@funnel_stage(StageEnum.DOWNLOAD, fallback=StageEnum.urlconf(StageEnum.RESULTS))
def download(request, session):
    return redirect(default_storage.url('%s.pdf' % session.slug))
