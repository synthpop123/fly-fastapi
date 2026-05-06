# FastAPI on Fly.io

![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=flat) ![Python Badge](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=fff&style=flat) ![uv Badge](https://img.shields.io/badge/uv-261230?logo=uv&logoColor=DE5FE9&style=flat) ![Ruff Badge](https://img.shields.io/badge/Ruff-D7FF64?logo=ruff&logoColor=000&style=flat) ![pre-commit Badge](https://img.shields.io/badge/pre--commit-FAB040?logo=precommit&logoColor=fff&style=flat) ![GitHub Actions Badge](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=fff&style=flat)

A minimal, production-ready FastAPI starter deployed on Fly.io.

- API endpoint: <https://fastapi.lkwplus.com>
- Swagger UI: <https://fastapi.lkwplus.com/docs>
- ReDoc: <https://fastapi.lkwplus.com/redoc>

## Stack

- Python 3.13, [FastAPI](https://fastapi.tiangolo.com/) (`fastapi[standard]`) with `lifespan`
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) for typed config
- [uv](https://docs.astral.sh/uv/) for dependency management & locking
- [Ruff](https://docs.astral.sh/ruff/) for linting & formatting, [pytest](https://docs.pytest.org/) + `httpx` for tests
- Multi-stage `Dockerfile` and Fly.io machine deploy with HTTP health checks

## Project layout

```
app/
├── core/         # configuration, logging
├── routers/      # API routers (root, health, ...)
├── schemas/      # Pydantic response/request models
├── services/     # business logic
└── main.py       # FastAPI factory + lifespan
tests/            # pytest + httpx async tests
```

## Getting started

```sh
git clone git@github.com:synthpop123/fly-fastapi.git
cd fly-fastapi

# Install dependencies (creates .venv automatically)
uv sync --all-groups

# Set up git hooks
uv run pre-commit install
```

## Run locally

```sh
# Dev mode (auto-reload)
uv run fastapi dev app/main.py

# Prod mode
uv run fastapi run app/main.py
```

## Lint, format, test

```sh
uv run ruff check .          # lint
uv run ruff format .         # format
uv run pytest                # run tests
uv run pre-commit run --all-files
```

## Deploy on Fly.io

```sh
fly launch     # first time only
fly deploy
```

The repository ships a Docker-based build (no buildpack required) and an HTTP
health check on `/health`. CI/CD is handled by GitHub Actions: `ci.yml` runs
lint and tests on every PR; `fly.yml` deploys on every push to `main` once the
`FLY_API_TOKEN` repository secret is configured.
