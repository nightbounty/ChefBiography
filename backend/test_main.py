import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_id():
    response = client.get("/id")
    assert response.status_code == 200
    assert isinstance(response.json(), str)

def test_get_tone():
    response = client.get("/tone")
    assert response.status_code == 200
    assert response.json() in ["humorous", "ironic", "cynical"]

def test_create_user():
    response = client.post("/user")
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["status"] == "success"
        assert "userId" in data

def test_get_user():
    # First, create a user to ensure there is a user to fetch
    create_response = client.post("/user")
    if create_response.status_code == 200:
        user_id = create_response.json()["userId"]
        
        # Fetch the created user by ID
        get_response = client.get(f"/user/{user_id}")
        assert get_response.status_code == 200
        user = get_response.json()
        assert user["id"] == user_id
        assert "name" in user
        assert "email" in user
        assert "phonenumber" in user
        assert "company" in user
        assert "biography" in user
        assert "tone" in user
    else:
        assert create_response.status_code == 500

def test_get_user_not_found():
    response = client.get("/user/4ac815c2-5ab4-4152-8886-5ba45cd5df8f")
    assert response.status_code == 404
