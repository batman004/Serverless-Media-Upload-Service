from fastapi.testclient import TestClient
from main import app
import os
client = TestClient(app)

def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200


def test_presigned_url(file="test.txt"):
    response = client.post(
            f"/api/upload/",
            headers={"Content-Type": "application/json"},
            json={"file_name": f"{file}"},
        )
    res = response.json()
    return res['presigned_url']

def test_upload(url=test_presigned_url()):
    path ="app/tests/test.txt"
    with open(f"{path}", 'r') as f:
        content = f.read()
    response = client.put(url, data=content)
    assert "Got response:"
    assert f"Status: {response.status_code}"


