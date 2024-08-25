#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lkw123"

from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


@router.get("/", summary="Hello, World!")
async def read_index():
    return {"message": "Hello, World!"}


@router.head("/", include_in_schema=False)
async def index():
    return {"message": "Hello, World!"}


@router.get(
    "/health",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).

    Returns:
        A JSON response with the health status
    """
    return HealthCheck(status="OK")
