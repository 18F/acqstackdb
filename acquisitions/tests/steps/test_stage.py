import pytest
from pytest_bdd import scenario, given, when, then
from pytest_factoryboy import register
from acquisitions import factories, models, forms
from functools import partial

register(factories.StageFactory)

scenario = partial(scenario, '../features/add_stage.feature')


@pytest.mark.django_db
@scenario()
