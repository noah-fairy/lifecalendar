from src.appl.dto import Resp
from src.appl.dto.calendar import CalendarResp
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


class GetCalendarListResp(Resp):
    calendars: list[CalendarResp]


class GetCalendarList:
    def __init__(self, db_context: IDBContext, calendar_repo: ICalendarRepo) -> None:
        self.db_context = db_context
        self.calendar_repo = calendar_repo

    def run(self) -> GetCalendarListResp:
        with self.db_context.begin_tx():
            cals = self.calendar_repo.get_all()
            return GetCalendarListResp(
                calendars=[CalendarResp.create(cal) for cal in cals]
            )
