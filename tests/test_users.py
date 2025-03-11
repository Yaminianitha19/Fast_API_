from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from app.main import app
from app import schemas
from app.config import settings



SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def override_get_db():
    db = TestingSessionLocal() 
    try:
        yield db
    finally:
        db.close()



from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Happy Coding! :)" 
    assert res.status_code == 200


def test_create_user():
    res = client.post("/users/", json={"email": "a@b.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "a@b.com"
    assert res.status_code == 201