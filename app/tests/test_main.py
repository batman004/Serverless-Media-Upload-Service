from fastapi.testclient import TestClient
from main import app
import os
client = TestClient(app)

os.environ['AWS_ACCESS_KEY_ID'] = "AKIAQJUTXMWPLCKKF322"
os.environ['AWS_SECRET_ACCESS_KEY'] = "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"
os.environ['AWS_DEFAULT_REGION'] = "ap-south-1"


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
    path ="test.txt"
    with open(f"{path}", 'r') as f:
        content = f.read()
    response = client.put(url, data=content)
    assert "Got response:"
    assert f"Status: {response.status_code}"


