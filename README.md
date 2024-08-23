# FastAPI on Fly.io

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
