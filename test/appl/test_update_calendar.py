import datetime
from unittest.mock import MagicMock

from src.appl.update_calendar import UpdateCalendar
from src.domain.entity.calendar import Calendar
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


class TestUpdateCalendar:
    def test_run(self):
        calendar = self._create_calendar()
        db_context = MagicMock(spec=IDBContext)
        calendar_repo = MagicMock(spec=ICalendarRepo)
        calendar_repo.get_or_error.return_value = calendar
        command = UpdateCalendar(db_context, calendar_repo)

        name = "뉴고도"
        birthday = datetime.date(2000, 6, 21)
        lifespan = 100
        command.run(calendar.id, name, birthday, lifespan)

        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan

    def _create_calendar(self) -> Calendar:
        return Calendar.create("고도", datetime.date(1988, 6, 21), 80)
