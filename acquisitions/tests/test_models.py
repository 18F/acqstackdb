import pytest
from acquisitions.models import Acquisition, Agency, Subagency

@pytest.mark.django_db
def test_create_acquisition():
    agency = Agency.objects.create(name = "Test Agency")
    subagency = Subagency.objects.create(name = "Test Subagency", agency = agency)
    acquisition = Acquisition.objects.create(
        agency = agency,
        subagency = subagency,
        task = "Build a test thing",
        award_status = 1
    )

    assert str(acquisition) == "Build a test thing (Test Subagency - Test Agency)"
