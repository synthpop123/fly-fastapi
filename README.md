# FastAPI on Fly.io

- API Endpoint: [https://api.lkwplus.com](https://api.lkwplus.com)
- Swagger-UI: [https://api.lkwplus.com/docs](https://api.lkwplus.com/docs)
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
