import uuid

from src.appl.dto import Resp
from src.appl.dto.calendar import CalendarDetailResp
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


class GetCalendarResp(Resp):
    calendar: CalendarDetailResp


class GetCalendar:
    def __init__(self, db_context: IDBContext, calendar_repo: ICalendarRepo) -> None:
        self.db_context = db_context
        self.calendar_repo = calendar_repo

    def run(self, calendar_id: uuid.UUID) -> GetCalendarResp:
        with self.db_context.begin_tx():
            cal = self.calendar_repo.get_or_error(calendar_id)
            return GetCalendarResp(calendar=CalendarDetailResp.create(cal))
