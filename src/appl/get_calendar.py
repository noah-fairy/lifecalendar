import datetime
import uuid

from src.appl.dto import Resp
from src.domain.entity.calendar import TimeType
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


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


class GetCalendarResp(Resp):
    calendar: CalendarResp


class GetCalendar:
    def __init__(self, db_context: IDBContext, calendar_repo: ICalendarRepo) -> None:
        self.db_context = db_context
        self.calendar_repo = calendar_repo

    def run(self, calendar_id: uuid.UUID) -> GetCalendarResp:
        with self.db_context.begin_tx():
            cal = self.calendar_repo.get_or_error(calendar_id)
            return GetCalendarResp(calendar=CalendarResp.create(cal))
