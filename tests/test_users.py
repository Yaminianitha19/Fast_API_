from app import schemas 
from .database import client, session

def test_root(client, session):
    
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Happy Coding! :)" 
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "a@b.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "a@b.com"
    assert res.status_code == 201

def test_login_user(client):
    res = client.post("/login", data={"username": "a@b.com", "password": "password123"})
    print(res.json())
    assert res.status_code == 200