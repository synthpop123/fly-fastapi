# FastAPI on Fly.io

![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=flat) ![Swagger Badge](https://img.shields.io/badge/Swagger-85EA2D?logo=swagger&logoColor=000&style=flat) ![Ruff Badge](https://img.shields.io/badge/Ruff-D7FF64?logo=ruff&logoColor=000&style=flat) ![pre-commit Badge](https://img.shields.io/badge/pre--commit-FAB040?logo=precommit&logoColor=fff&style=flat) ![GitHub Actions Badge](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=fff&style=flat)

- API Endpoint: [https://api.lkwplus.com](https://api.lkwplus.com)
- Swagger UI: [https://api.lkwplus.com/docs](https://api.lkwplus.com/docs)
- Redoc: [https://api.lkwplus.com/redoc](https://api.lkwplus.com/redoc)

## Clone GitHub repo

```sh
git clone git@github.com:synthpop123/fly-fastapi.git
cd fly-fastapi
```

## Install dependencies

```sh
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt

# Install pre-commit
pre-commit install

# Test pre-commit function
pre-commit run --all-files
```

## Run locally

```sh
# Dev mode
fastapi dev

# Prod mode
fastapi run
```

## Launching on Fly.io

```sh
# Launch on fly.io
fly launch

# Deploy on fly.io
fly deploy
```

## GitHub Actions

Create a repository secret `FLY_API_TOKEN`, the value should be the deploy token generated from the fly.io dashboard.

Once `git push` is triggered, GitHub Actions will automatically run `fly deploy`.
