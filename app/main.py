from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI

from app.core.config import Settings, get_settings
from app.core.logging import configure_logging
from app.routers import health, root

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings: Settings = get_settings()
    configure_logging("DEBUG" if settings.debug else "INFO")
    logger.info(
        "Starting %s v%s (%s)", settings.app_name, settings.app_version, settings.environment
    )
    yield
    logger.info("Shutting down %s", settings.app_name)


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
        contact={"name": "lkw123", "email": "me@lkwplus.com"},
        lifespan=lifespan,
    )

    app.include_router(root.router)
    app.include_router(health.router)

    return app


app = create_app()
