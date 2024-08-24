#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lkw123"

from fastapi import FastAPI

from routers.root import router as root_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI",
        description="FastAPI on Fly.io",
        version="0.0.1",
        contact={
            "name": "lkw123",
            "email": "me@lkwplus.com",
        },
    )

    # include all routers
    app.include_router(root_router, prefix="", tags=["root"])
    # TODO: include other routers here

    return app


app = create_app()
