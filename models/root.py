#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lkw123"

from pydantic import BaseModel


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"
