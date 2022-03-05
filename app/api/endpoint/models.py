from pydantic import BaseModel

class UploadFile(BaseModel):
  file_name: str