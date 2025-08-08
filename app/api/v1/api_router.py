from fastapi import APIRouter
from .endpoints import example

router = APIRouter()

# Include your routers here
router.include_router(example.router, prefix="/example", tags=["Example"])
