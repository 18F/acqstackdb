import pytest
from django.core.exceptions import ValidationError
from acquisitions.models import Acquisition, Agency, Subagency,\
                                Vendor, AwardStatus, Track


@pytest.mark.django_db
def test_create_acquisition():
    agency = Agency.objects.create(name="Test Agency")
    subagency = Subagency.objects.create(name="Test Subagency", agency=agency)
    track = Track.objects.create(name="Test Track")
    award_status = AwardStatus.objects.create(name="Qualifying", owner='18F',
                                              track=track)
    acquisition = Acquisition.objects.create(
        agency=agency,
        subagency=subagency,
        task="Build a test thing",
        award_status=award_status,
        track=track
    )

    assert str(acquisition) == "Build a test thing " + \
                               "(Test Subagency - Test Agency)"


@pytest.mark.django_db
def test_correct_track():
    with pytest.raises(ValidationError):
        agency = Agency.objects.create(name="Test Agency")
        subagency = Subagency.objects.create(name="Test Subagency",
                                             agency=agency)
        track = Track.objects.create(name="Test Track")
        track2 = Track.objects.create(name="The Other Track")
        award_status = AwardStatus.objects.create(name="Qualifying",
                                                  owner='18F', track=track2)
        acquisition = Acquisition.objects.create(
            agency=agency,
            subagency=subagency,
            task="Build a test thing",
            award_status=award_status,
            track=track
        )

        acquisition.full_clean()
        assert str(acquisition) == "Build a test thing " + \
                                   "(Test Subagency - Test Agency)"


@pytest.mark.django_db
def test_create_vendor():
    vendor = Vendor.objects.create(
        name="Test Vendor",
        email="testvendor@fake.biz",
        duns=123456789
    )

    vendor.full_clean()
    assert str(vendor) == "Test Vendor"


@pytest.mark.django_db
def test_bad_duns():
    with pytest.raises(ValidationError):
        bad_duns_vendor = Vendor.objects.create(
            name="Bad DUNS Vendor",
            email="testvendor@fake.biz",
            duns=666
        )

        bad_duns_vendor.full_clean()
        assert str(bad_duns_vendor) == "Bad DUNS Vendor"
