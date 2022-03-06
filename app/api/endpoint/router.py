from fastapi import APIRouter
from .models import UploadFile
from ..upload.helper import upload_file
import os
#router object for handling api routes
router = APIRouter()


@router.post("/")
async def handle_upload_put(file: UploadFile):
  uploaded = upload_file(file)
  return uploaded