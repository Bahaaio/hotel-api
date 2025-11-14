from fastapi import APIRouter
from app.models.health import HealthResponse


router = APIRouter(prefix="/health")


@router.get("")
def health() -> HealthResponse:
    return HealthResponse()
