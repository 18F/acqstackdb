import pytest
from acquisitions.views import home

@pytest.mark.django_db
def test_home(rf):
    request = rf.get('/')
    response = home(request)
    assert response.status_code == 200
