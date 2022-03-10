from fastapi import APIRouter, Depends
from .models import UploadFile, User, Login, Token
from ..upload.helper import upload_file
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from ..auth.jwt_token import create_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#router object for handling api routes
router = APIRouter()


@router.post("/")
async def handle_upload_put(file: UploadFile = Depends(oauth2_scheme)):
  uploaded = upload_file(file)
  return uploaded

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = create_access_token(data={"user": form_data.username })
    return {"access_token": access_token, "token_type": "bearer"}
