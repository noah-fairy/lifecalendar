import datetime
import uuid

from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


class UpdateCalendar:
    def __init__(self, db_context: IDBContext, calendar_repo: ICalendarRepo) -> None:
        self.db_context = db_context
        self.calendar_repo = calendar_repo

    def run(
        self, calendar_id: uuid.UUID, name: str, birthday: datetime.date, lifespan: int
    ) -> None:
        with self.db_context.begin_tx():
            calendar = self.calendar_repo.get_or_error(calendar_id)
            calendar.update_basic_info(name, birthday, lifespan)
