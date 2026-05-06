from typing import Literal

from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    """Response payload for health check endpoint."""

    status: Literal["ok"] = Field(default="ok", description="Service liveness indicator")
