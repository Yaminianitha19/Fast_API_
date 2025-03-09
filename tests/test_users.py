from fastapi.testclient import TestClient
from fastapi import HTTPException

from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Happy Coding! :)" 
    assert res.status_code == 200