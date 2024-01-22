import requests
from api import app

ENDPOINT = "http://127.0.0.1:5000"

# GET users (test)
def test_get_users():
    with app.app_context():
        response = requests.get(f"{ENDPOINT}/users")
        actual = response.json()        
        assert response.status_code == 200
        for user in actual:
            assert "id" in user
            assert "name" in user
        
# GET user by user ID (test)
def test_get_user_by_id():
    with app.app_context():
        response = requests.get(f"{ENDPOINT}/users/1")
        actual = response.json()
        assert response.status_code == 200
        assert actual["id"] == 1

# GET user by user ID, invalid ID test
def test_get_user_by_id_invalid_id():
    expected = { 'error': 'User does not exist'}
    
    with app.app_context():
        response = requests.get(f"{ENDPOINT}/users/111")
        actual = response.json()
        assert response.status_code == 404
        assert actual == expected

# POST a new user (test)
def test_post_new_user():
    
    user_data = {
        "name": "Meghan"
    }
    
    with app.app_context():
        response = requests.post(f"{ENDPOINT}/users", json=user_data)
        assert response.status_code == 201

# POST a new user, invalid user properties test
def test_post_new_user_invalid_properties():
    user_data = {
        "nickname": "Meghan the Maverick"
    }
    expected = { 'error': 'Invalid user properties.' }
    with app.app_context():
        response = requests.post(f"{ENDPOINT}/users", json=user_data)
        actual = response.json()
        assert actual == expected
        assert response.status_code == 400
        
# DELETE a user by ID (test)
def test_delete_user():
    with app.app_context():
        response = requests.delete(f"{ENDPOINT}/users/1")
        actual = response.json()
        assert response.status_code == 200
        for user in actual:
            assert "id" in user != 1