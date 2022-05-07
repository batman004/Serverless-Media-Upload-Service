from fastapi import APIRouter, Depends, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .models import UploadFile, User, Login
from upload.helper import upload_file
from auth.hashing import Hash
from auth.helper import check_user
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT

#router object for handling api routes
router = APIRouter()

# generate pre-signed url
@router.post("/service/upload", dependencies=[Depends(JWTBearer())], response_description="get the pre-signed url")
async def handle_upload_put(file: UploadFile):
  uploaded = upload_file(file)
  return uploaded

# login + get token
@router.post("/auth/login")
async def login_for_access_token(request: Request, user_to_login: Login):
    user = await check_user(request, user_to_login)
    await request.app.mongodb["users"].update_one(
    {"_id": user["_id"]}, {"$set": user}
    )
    return signJWT(user["email"])

#logout 
@router.post("/auth/logout", dependencies=[Depends(JWTBearer())], response_description="Logout of the app")
async def logout(username: str, request: Request):
    user = await request.app.mongodb["users"].find_one({"username":username})
    user["disabled"]=True
    await request.app.mongodb["users"].update_one(
    {"_id": user["_id"]}, {"$set": user}
    )
    return{"message":f"user: {username} logged out"}


#signup
@router.post("/auth/signup", response_description="Signup for a new user")
async def create_user(request: Request, user: User):
    user = jsonable_encoder(user)
    user["disabled"]=True
    hashed_pass = Hash.bcrypt(user["password"])
    user["password"] = hashed_pass
    new_user = await request.app.mongodb["users"].insert_one(user)
    created_user = await request.app.mongodb["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
