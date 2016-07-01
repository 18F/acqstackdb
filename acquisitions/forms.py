import floppyforms.__future__ as forms
from acquisitions import models


class AcquisitionForm(forms.ModelForm):
    class Meta:
        model = models.Acquisition
        # fields = ['subagency', 'track', 'task', 'step']
        exclude = []


class TrackForm(forms.ModelForm):
    class Meta:
        model = models.Track
        fields = ['name']


class StageForm(forms.ModelForm):
    class Meta:
        model = models.Stage
        fields = ['name']


class StepForm(forms.ModelForm):
    class Meta:
        model = models.Step
        fields = ['actor']


class AgencyForm(forms.ModelForm):
    class Meta:
        model = models.Agency
        fields = ['name']


class SubagencyForm(forms.ModelForm):
    class Meta:
        model = models.Subagency
        fields = ['agency', 'name']


class ActorForm(forms.ModelForm):
    class Meta:
        model = models.Actor
        fields = ['name']
