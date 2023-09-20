from fastapi import APIRouter

api_router_v1 = APIRouter(prefix="/v1")


@api_router_v1.get("/")
async def api_root():
    return dict(path="/api/v1", status="ok")
