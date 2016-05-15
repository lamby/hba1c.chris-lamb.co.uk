from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from hba1c.utils.ajax import ajax
from hba1c.session.enums import StageEnum
from hba1c.session.decorators import funnel_stage

from hba1c.session.models import Session

from .forms import ResultForm, DoneForm

@funnel_stage(StageEnum.RESULTS)
def view(request, session):
    if request.method == 'POST':
        form = ResultForm(session, request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Result added.")

            return redirect(request.path)
    else:
        form = ResultForm(session)

    return render(request, 'results/view.html', {
        'form': form,
        'session': session,
    })

@require_POST
@funnel_stage(StageEnum.RESULTS)
def done(request, session):
    form = DoneForm(session, request.POST)

    if not form.is_valid():
        return redirect(StageEnum.urlconf(StageEnum.RESULTS))

    # Generate the PDF asynchronously
    form.save()

    return Session.objects.set_and_redirect(request, StageEnum.PREVIEW)

@require_POST
@funnel_stage(StageEnum.RESULTS)
def delete(request, session, result_id):
    get_object_or_404(session.results, pk=result_id).delete()

    messages.info(request, "Result deleted.")

    return redirect(StageEnum.urlconf(StageEnum.RESULTS))
