from acquisitions.views import home

def test_home(rf):
    request = rf.get('/')
    response = home(request)
    assert response.status_code == 200
