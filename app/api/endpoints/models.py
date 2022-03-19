import uuid
from pydantic import BaseModel, Field
from typing import Optional

class UploadFile(BaseModel):
  file_name: str

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: str
    disabled: Optional[bool] = None

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None