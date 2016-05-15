from django import forms

from hba1c.session.models import Session

class NameForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = (
            'name',
        )
