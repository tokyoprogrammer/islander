import requests
def test_request():
    response = requests.get('https://httpbin.org/ip')
    assert response.status_code == 200

