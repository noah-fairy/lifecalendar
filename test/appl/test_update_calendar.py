import datetime
import uuid

from src.appl.cal.update_calendar import UpdateCalendar
from src.appl.i_container import IContainer
from src.domain.entity.calendar import Calendar


class TestUpdateCalendar:
    def test_run(self, container: IContainer):
        user_id = uuid.uuid4()

        command = container.resolve(UpdateCalendar)
        calendar = self._create_calendar(user_id)
        command.calendar_repo.get_by_id_and_user_id_or_error.return_value = calendar

        name = "뉴고도"
        birthday = datetime.date(2000, 6, 21)
        lifespan = 100
        command.run(user_id, calendar.id, name, birthday, lifespan)

        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan

    def _create_calendar(self, user_id: uuid.UUID) -> Calendar:
        return Calendar.create(user_id, "고도", datetime.date(1988, 6, 21), 80)
