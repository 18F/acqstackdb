import pytest
from acquisitions.models import AwardStatus, Track


@pytest.mark.django_db
def test_add_award_status():
    track = Track.objects.create(name="Test Track")
    status1 = AwardStatus.objects.create(status="Test 1", actor="Nobody",
                                         track=track)
    status2 = AwardStatus.objects.create(status="Test 2", actor="Nobody",
                                         track=track)

    assert status1.ordering == 0
    assert status2.ordering == 1

    status3 = AwardStatus.objects.create(status="Test 3", actor="Nobody",
                                         track=track, is_before=status2)
    status2 = AwardStatus.objects.get(status="Test 2")

    assert status3.ordering == 1
    assert status2.ordering == 2


@pytest.mark.django_db
def test_remove_award_status():
    track = Track.objects.create(name="Test Track")
    status1 = AwardStatus.objects.create(status="Test 1", actor="Nobody",
                                         track=track)
    status2 = AwardStatus.objects.create(status="Test 2", actor="Nobody",
                                         track=track)
    status3 = AwardStatus.objects.create(status="Test 3", actor="Nobody",
                                         track=track, is_before=status2)

    delete = AwardStatus.objects.filter(status="Test 3").delete()

    assert status1.ordering == 0
    assert status2.ordering == 1


@pytest.mark.django_db
def test_add_to_other_track():
    track1 = Track.objects.create(name="Test Track 1")
    track2 = Track.objects.create(name="Test Track 2")
    status1 = AwardStatus.objects.create(status="Test 1", actor="Nobody",
                                         track=track1)
    status2 = AwardStatus.objects.create(status="Test 2", actor="Nobody",
                                         track=track2)

    assert status1.ordering == 0
    assert status2.ordering == 0
