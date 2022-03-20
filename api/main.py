import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from motor.motor_asyncio import AsyncIOMotorClient
from api.config import settings 
from api.endpoints.router import router as upload_router

app = FastAPI()

@app.get("/", tags=["Endpoint test"])
def read_root():
    return {"message":"welcome to Media-Upload-Service Backend !"}

app.include_router(upload_router, tags=["services"], prefix="/api")

@app.on_event("startup")
async def startup_db_client():
  #initiate mangum obj for AWS
    handler = Mangum(app=app)
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )



