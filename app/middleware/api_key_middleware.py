from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import os

class APIKeyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, api_key_header: str = "X-API-Key"):
        super().__init__(app)
        self.api_key_header = api_key_header
        self.valid_api_key = os.getenv("API_KEY", "super-secret-key")  # fallback for testing

    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get(self.api_key_header)

        if api_key != self.valid_api_key:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or missing API key"},
            )

        return await call_next(request)