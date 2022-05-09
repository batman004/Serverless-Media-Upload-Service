import os

from fastapi.testclient import TestClient
from api.main import app

import os
client = TestClient(app)


def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200
    assert response_auth.json() == {"message": "welcome to Media-Upload-Service Backend !"}


def get_auth_token():
    response = client.post(
        f"api/auth/login",
        headers={"Content-Type": "application/json"},
        json={"username": "John",
              "password": os.getenv['ADMIN_PASSWORD']
              },
    )

    res = response.json()
    return res['access_token']


def test_presigned_url(file="test.txt", auth_token=get_auth_token()):
    response = client.post(
        f"api/service/upload",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        },
        json={"file_name": f"{file}"},
    )
    res = response.json()
    return res['presigned_url']


def test_upload(url=test_presigned_url()):
    path = "tests/test.txt"
    with open(f"{path}", 'r') as f:
        content = f.read()
    response = client.put(url, data=content)
    assert "Got response:"
    assert f"Status: {response.status_code}"
