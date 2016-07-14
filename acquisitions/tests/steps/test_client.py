import pytest
from pytest_bdd import scenario, given, when, then
from pytest_factoryboy import register
from acquisitions import factories, models, forms
from functools import partial

register(factories.AgencyFactory, 'client_agency')
register(factories.SubagencyFactory, 'client_subagency')


@pytest.fixture
def client_subagency__agency(client_agency):
    return client_agency

scenario = partial(scenario, '../features/add_client.feature')


@pytest.mark.django_db
@scenario('Submitting a client with a form')
@scenario('Creating a client')
def test_client():
    pass


@given('an agency exists')
def create_agency(client_agency):
    return client_agency


@when('a user creates a subagency')
def create_subagency(client_subagency):
    return client_subagency


@when('a user submits a valid subagency form')
def submit_subagency_form(client_agency):
    form = forms.SubagencyForm(data={
        'agency': client_agency.id,
        'name': 'Test Subagency'
    })
    assert form.is_valid() == True
    client_subagency = form.save()
    return client_subagency


@then('the subagency is saved in the database')
def subagency_is_saved(client_subagency, client_agency):
    assert isinstance(client_subagency, models.Subagency)
    assert client_subagency.agency == client_agency
