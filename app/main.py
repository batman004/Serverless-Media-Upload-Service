import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from api.endpoint.router import router as upload_router

app = FastAPI()

@app.get("/", tags=["Endpoint test"])
def read_root():
    return {"message":"welcome to Media-Upload-Service Backend !"}

app.include_router(upload_router, tags=["services"], prefix="/api/upload")

@app.on_event("startup")
async def startup_db_client():
  #initiate mangum obj for AWS
  handler = Mangum(app=app)




