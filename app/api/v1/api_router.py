from fastapi import APIRouter
from .endpoints import onboarding

router = APIRouter()

router.include_router(onboarding.router, prefix="/onboarding", tags=["Onboarding"])
