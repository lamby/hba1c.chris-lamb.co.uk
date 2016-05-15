import datetime

from django import forms
from django.db import transaction

from hba1c.reports.tasks import generate_pdf_and_previews

from .models import Result

DATE_CUTOFF = datetime.date(2000, 1, 1)
VALUE_MIN, VALUE_MAX = 20, 150

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = (
            'date',
            'value',
        )

    def __init__(self, session, *args, **kwargs):
        self.session = session

        super(ResultForm, self).__init__(*args, **kwargs)

    def clean_date(self):
        val = self.cleaned_data['date']

        if self.session.results.filter(date=val).exists():
            raise forms.ValidationError(
                "A result with that date already exists",
            )

        if val > datetime.date.today():
            raise forms.ValidationError("Date is in the future.")

        if val < DATE_CUTOFF:
            raise forms.ValidationError("Date is too far in the past.")

        return val

    def clean_value(self):
        val = self.cleaned_data['value']

        if val > VALUE_MAX:
            raise forms.ValidationError("Result value is too high.")

        if val < VALUE_MIN:
            raise forms.ValidationError("Result value is too low.")

        return val

    def save(self):
        instance = super(ResultForm, self).save(commit=False)
        instance.session = self.session
        instance.save()

        return instance

class DoneForm(forms.Form):
    def __init__(self, session, *args, **kwargs):
        self.session = session

        super(DoneForm, self).__init__(*args, **kwargs)

    def save(self):
        session = self.session

        session.generating_pdf = True
        session.save(update_fields=('generating_pdf',))
        transaction.on_commit(
            lambda: generate_pdf_and_previews.delay(session.slug)
        )
