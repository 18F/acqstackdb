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
    track = forms.ModelMultipleChoiceField(queryset=models.Track.objects.all())

    class Meta:
        model = models.Step
        exclude = []

    def save(self, commit=True):
        # step = super(StepForm, self).save()
        form_data = self.cleaned_data
        step = models.Step.objects.create(
            stage=form_data["stage"],
            actor=form_data["actor"]
        )
        for track in form_data["track"]:
            models.StepTrackThroughModel.objects.create(
                step=step,
                track=track
            )


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
