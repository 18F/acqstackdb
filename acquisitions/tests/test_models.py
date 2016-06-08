import pytest
from django.core.exceptions import ValidationError
from acquisitions.models import Acquisition, Agency, Subagency, Vendor

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

@pytest.mark.django_db
def test_create_vendor():
    vendor = Vendor.objects.create(
        name = "Test Vendor",
        email = "testvendor@fake.biz",
        duns = 123456789
    )

    vendor.full_clean()
    assert str(vendor) == "Test Vendor"

@pytest.mark.django_db
def test_bad_duns():
    with pytest.raises(ValidationError):
        bad_duns_vendor = Vendor.objects.create(
            name = "Bad DUNS Vendor",
            email = "testvendor@fake.biz",
            duns = 666
        )

        bad_duns_vendor.full_clean()
        assert str(bad_duns_vendor) == "Bad DUNS Vendor"
