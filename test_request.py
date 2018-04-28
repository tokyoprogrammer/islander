import requests
def test_request():
    response = requests.get('https://www.google.com')
    assert response.status_code == 200

