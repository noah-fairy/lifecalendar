import datetime
import uuid

from src.appl.dto import Resp
from src.domain.entity.calendar import TimeType


class WeekResp(Resp):
    yearnum: int
    weeknum: int
    today: datetime.date
    birthday: datetime.date
    lifespan: int

    time_type: TimeType


class YearResp(Resp):
    yearnum: int
    weeks: list[WeekResp]


class CalendarResp(Resp):
    id: uuid.UUID
    name: str
    birthday: datetime.date
    lifespan: int

    years: list[YearResp]
