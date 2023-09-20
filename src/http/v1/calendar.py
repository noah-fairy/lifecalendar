import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from src.appl.container import container
from src.appl.create_calendar import CreateCalendar

api_router_calendar = APIRouter(prefix="/calendar")


class CreateCalendarReq(BaseModel):
    name: str
    birthday: datetime.date
    lifespan: int


@api_router_calendar.post("/create")
async def create(req: CreateCalendarReq):
    container.resolve(CreateCalendar).run(req.name, req.birthday, req.lifespan)
