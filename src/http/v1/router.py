from fastapi import APIRouter

from src.http.v1.calendar import api_router_calendar

api_router_v1 = APIRouter(prefix="/v1")
api_router_v1.include_router(api_router_calendar)


@api_router_v1.get("/")
async def api_root():
    return dict(path="/api/v1", status="ok")
