import datetime
import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from src.appl.cal.create_calendar import CreateCalendar
from src.appl.cal.get_calendar import GetCalendar, GetCalendarResp
from src.appl.cal.get_calendar_list import GetCalendarList, GetCalendarListResp
from src.appl.cal.update_calendar import UpdateCalendar
from src.appl.container import container

api_router_calendar = APIRouter(prefix="/calendar")


@api_router_calendar.get("", response_model=GetCalendarListResp)
async def get_list():
    return container.resolve(GetCalendarList).run()


class CreateCalendarReq(BaseModel):
    name: str
    birthday: datetime.date
    lifespan: int


@api_router_calendar.post("/create")
async def create(req: CreateCalendarReq):
    container.resolve(CreateCalendar).run(req.name, req.birthday, req.lifespan)


@api_router_calendar.get("/{calendar_id}", response_model=GetCalendarResp)
async def get(calendar_id: uuid.UUID):
    return container.resolve(GetCalendar).run(calendar_id)


class UpdateCalendarReq(BaseModel):
    name: str
    birthday: datetime.date
    lifespan: int


@api_router_calendar.post("/{calendar_id}/update")
async def update(calendar_id: uuid.UUID, req: UpdateCalendarReq):
    container.resolve(UpdateCalendar).run(
        calendar_id, req.name, req.birthday, req.lifespan
    )
