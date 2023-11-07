import datetime

from src.domain.entity.calendar import Calendar
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


class CreateCalendar:
    def __init__(self, db_context: IDBContext, calendar_repo: ICalendarRepo) -> None:
        self.db_context = db_context
        self.calendar_repo = calendar_repo

    def run(self, name: str, birthday: datetime.date, lifespan: int) -> None:
        with self.db_context.begin_tx():
            cal = Calendar.create(name, birthday, lifespan)
            self.calendar_repo.save(cal)
