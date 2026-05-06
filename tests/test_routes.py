from httpx import AsyncClient


async def test_read_index(client: AsyncClient) -> None:
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


async def test_head_index(client: AsyncClient) -> None:
    response = await client.head("/")
    assert response.status_code == 200


async def test_health(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


async def test_openapi_schema(client: AsyncClient) -> None:
    response = await client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "FastAPI"
    assert "/health" in schema["paths"]
