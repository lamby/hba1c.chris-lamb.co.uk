from django.shortcuts import render

from hba1c.session.enums import StageEnum
from hba1c.session.decorators import funnel_stage

from hba1c.session.models import Session

@funnel_stage(StageEnum.PREVIEW, fallback=StageEnum.urlconf(StageEnum.RESULTS))
def view(request, session):
    if request.method == 'POST':
        return Session.objects.set_and_redirect(request, StageEnum.DOWNLOAD)

    return render(request, 'reports/preview/view.html', {
        'session': session,
    })

