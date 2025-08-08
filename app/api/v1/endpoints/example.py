from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def example_endpoint():
    return {"message": "This is an example endpoint"}
