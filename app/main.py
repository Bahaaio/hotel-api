from fastapi import FastAPI
from .routers.hotels import router as hotel_router
from .routers.availability import router as availability_router
from .routers.health import router as health_router

app = FastAPI()

app.include_router(hotel_router)
app.include_router(availability_router)
app.include_router(health_router)
