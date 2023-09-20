from fastapi import FastAPI

from src.http.v1.router import api_router_v1

app = FastAPI()


@app.get("/")
async def root():
    return dict(path="/", status="ok")


api = FastAPI()  # for /api prefix
api.include_router(api_router_v1)
app.mount("/api", api)
