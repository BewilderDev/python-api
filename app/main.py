from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from routes.routers import router
from database.database import MongoConnection
from middleware.api_key_middleware import APIKeyMiddleware
import logging

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    MongoConnection.get_client()
    print("MongoDB connected")

    yield  # Wait here until the app shuts down

    # Shutdown
    MongoConnection.close_connection()
    print("MongoDB connection closed")

app = FastAPI(title="ChatBot API", version="1.0.0")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(APIKeyMiddleware)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)