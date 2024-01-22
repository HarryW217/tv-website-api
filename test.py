import requests
from api import app

ENDPOINT = "http://127.0.0.1:5000"

def test_get_users():
    expected = [
        {'id': 1, 'name': 'Harry'},
        {'id': 2, 'name': 'Zach'},
        {'id': 3, 'name': 'Walter'}
    ]

    with app.app_context():

        response = requests.get(f"{ENDPOINT}/users")
        actual = response.json()
        
        assert response.status_code == 200
        assert actual == expected
        

    