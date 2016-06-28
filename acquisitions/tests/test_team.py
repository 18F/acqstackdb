import pytest
from django.contrib.auth.models import User
from acquisitions.models import Acquisition, Agency, Subagency, Vendor, \
                                Role, Step, Stage, Track, Actor


@pytest.fixture
def test_user():
    user = User.objects.create_user(username='test_user',
                                    email='', password='')
    return user


@pytest.fixture
def role(test_user):
    role = Role.objects.create(description='A', teammate=test_user)
    return role


@pytest.fixture
def acquisition():
    agency = Agency.objects.create(name="Test Agency")
    subagency = Subagency.objects.create(name="Test Subagency", agency=agency)
    track = Track.objects.create(name="Test Track")
    stage = Stage.objects.create(name="Test Stage")
    actor = Actor.objects.create(name="Test Actor")
    step = Step.objects.create(
        stage=stage,
        actor=actor,
        track=track
    )
    acquisition = Acquisition.objects.create(
        agency=agency,
        subagency=subagency,
        task="Build a test thing",
        step=step,
        track=track
    )
    return acquisition


@pytest.mark.django_db
def test_role_created(role, test_user):
    assert isinstance(role, Role)
    assert role.description == 'A'
    assert role.teammate == test_user


@pytest.mark.django_db
def test_add_role_to_acquisition(acquisition, role):
    '''
    Test to see whether a role object is properly added to the acquisition
    '''
    assert isinstance(acquisition, Acquisition)
    assert len(acquisition.roles.all()) == 0    # Confirm no existing roles

    # Add the role
    acquisition.roles.add(role)

    # Confirm that the role is added
    results = acquisition.roles.all()
    assert len(results) == 1
    assert results[0] == role
    assert str(results[0]) == "Acquisition Lead - test_user"
