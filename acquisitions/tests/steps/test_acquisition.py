import pytest
from pytest_bdd import scenario, given, when, then
from pytest_factoryboy import register
from acquisitions import factories, models, forms
from functools import partial

register(factories.AgencyFactory)
register(factories.SubagencyFactory)
register(factories.TrackFactory)
register(factories.StageFactory)
register(factories.ActorFactory)
register(factories.StepFactory)
register(factories.StepTrackThroughFactory)
register(factories.AcquisitionFactory)
register(factories.SubagencyFactory)

scenario = partial(scenario, '../features/add_acquisition.feature')


@pytest.mark.django_db
# @scenario('Submitting an acquisition with a form')
@scenario('Creating an acquisition')
def test_acquisition():
    pass


@given('a client exists')
def client(agency, subagency):
    # print(agency)
    # print(subagency)
    return agency, subagency


@given('a filled-in track exists')
def complete_track(track, stage, actor, step, step_track_through_model):
    return track, stage, actor, step, step_track_through_model


@when('a user creates an acquisition')
def create_acquisition(acquisition):
    return acquisition


@when('a user submits a valid acquisition form')
def submit_acquisition_form(subagency, track, step):
    form = forms.AcquisitionForm(data={
        'subagency': subagency.id,
        'track': track.id,
        'step': step.id,
        'task': 'Test Task'
    })
    assert form.is_valid() == True
    acquisition = form.save()
    return acquisition


@then('the acquisition is saved in the database')
def acquisition_is_saved(acquisition):
    assert isinstance(acquisition, models.Acquisition)
    # assert acquisition.task == 'Test Task'
