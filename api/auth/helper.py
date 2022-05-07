from fastapi import Request, HTTPException, status
from endpoints.models import Login
from .hashing import Hash

async def check_user(request: Request, user_to_login: Login):
    user = await request.app.mongodb["users"].find_one({"username":user_to_login.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with username: {user_to_login.username}')
    if not Hash.verify(user["password"],user_to_login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
    return user