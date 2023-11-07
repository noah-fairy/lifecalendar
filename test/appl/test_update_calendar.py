import datetime
import uuid

from src.appl.cal.update_calendar import UpdateCalendar
from src.appl.i_container import IContainer
from src.domain.entity.calendar import Calendar


class TestUpdateCalendar:
    def test_run(self, container: IContainer):
        command = container.resolve(UpdateCalendar)
        calendar = self._create_calendar()
        command.calendar_repo.get_or_error.return_value = calendar

        name = "뉴고도"
        birthday = datetime.date(2000, 6, 21)
        lifespan = 100
        command.run(calendar.id, name, birthday, lifespan)

        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan

    def _create_calendar(self) -> Calendar:
        return Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)
