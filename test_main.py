from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


def test_read_item_with_query():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}


def test_create_item():
    response = client.post("/items", json={"item_id": 42, "q": "test"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}


def test_create_item_with_default_q():
    response = client.post("/items", json={"item_id": 42})
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}