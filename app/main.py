import uvicron
from pyngrok import conf, ngrok
from fastapi import FastAPI
from mangum import Mangum
from config import settings

from app.api.endpoint.router import router as upload_router

app = FastAPI()

@app.get("/", tags=["Endpoint test"])
def read_root():
    return {"message":"welcome to Media-Upload-Service Backend !"}

@app.on_event("startup")
async def startup_db_client():
  #initiate mangum obj for AWS
  handler = Mangum(app=app)

app.include_router(upload_router, tags=["services"], prefix="/upload")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )







