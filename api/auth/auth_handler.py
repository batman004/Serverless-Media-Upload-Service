import time
from typing import Dict
import jwt
import os

def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, os.getenv["JWT_SECRET_KEY"], algorithm=os.getenv["JWT_ALGORITHM"])

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, os.getenv["JWT_SECRET_KEY"], algorithms=os.getenv["JWT_ALGORITHM"])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except jwt.InvalidTokenError:
        return {"Not verified"}
