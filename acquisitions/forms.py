import floppyforms.__future__ as forms
from .models import Acquisition


class AcquisitionForm(forms.ModelForm):
    class Meta:
        model = Acquisition
        fields = ['subagency', 'task', 'step']
