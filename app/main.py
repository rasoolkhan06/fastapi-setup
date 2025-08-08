from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import configs

app = FastAPI()

# Configure CORS
if configs.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
