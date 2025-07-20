from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from routes.routers import router  # Changed from relative to absolute import
import logging

app = FastAPI(title="ChatBot API", version="1.0.0")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(GZipMiddleware, minimum_size=1000)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(router)
