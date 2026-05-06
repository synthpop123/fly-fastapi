from fastapi import APIRouter, status

from app.schemas import HealthCheck

router = APIRouter(tags=["health"])


@router.get(
    "/health",
    summary="Perform a health check",
    response_description="Service is reachable",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """Lightweight liveness probe used by Fly.io and container orchestrators."""
    return HealthCheck()
