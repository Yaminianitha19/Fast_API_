import pytest
from jose import jwt
from app import schemas 
from app.config import settings

# def test_root(client, session):
#     res = client.get("/")
#     print(res.json().get("message"))
#     assert res.json().get("message") == "Happy Coding! :)" 
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "a@b.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "a@b.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",[
    ('wrongemail@gmail.com', 'password123', 403),
    ('a@b.com', 'wrongpassword', 403)])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    assert res.json().get('detail') == "invalid credentials"

def test_missing_username(client):
    res = client.post("/login", data={"password": "password123"})
    assert res.status_code == 422

def test_missing_password(client):
    res = client.post("/login", data={"username": "a@b.com"})
    assert res.status_code == 422