from fastapi import FastAPI

from src.appl.container import compose_container
from src.http.v1.router import api_router_v1
from src.infra.db.mapper import map_between_model_and_schema

map_between_model_and_schema()
compose_container()
app = FastAPI()


@app.get("/")
async def root():
    return dict(path="/", status="ok")


api = FastAPI()  # for /api prefix
api.include_router(api_router_v1)
app.mount("/api", api)
