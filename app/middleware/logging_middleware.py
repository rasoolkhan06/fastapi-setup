import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request
        start_time = time.time()
        logger.info(f"Incoming request: {request.method} {request.url}")
        
        # Process request
        response = await call_next(request)
        
        # Calculate processing time
        process_time = (time.time() - start_time) * 1000
        formatted_process_time = f"{process_time:.2f}ms"
        
        # Log response
        logger.info(
            f"Request completed: {request.method} {request.url} "
            f"Status: {response.status_code} "
            f"Duration: {formatted_process_time}"
        )
        
        # Add header with process time
        response.headers["X-Process-Time"] = formatted_process_time
        return response
