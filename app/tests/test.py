from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200


def test_upload_service():
    response_auth = client.get(f"/api/upload")
    assert response_auth.status_code == 200
