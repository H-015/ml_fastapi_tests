from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tests():
    response = client.get("/tests")
    assert response.status_code == 200
    assert response.json() == []

def test_create_test():
    response = client.post("/tests", json={"id": 1, "name": "Test 1"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test 1"}
