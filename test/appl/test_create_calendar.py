import datetime

from src.appl.create_calendar import CreateCalendar
from src.appl.i_container import IContainer


class TestCreateCalendar:
    def test_run(self, container: IContainer):
        command = container.resolve(CreateCalendar)

        name = "고도"
        birthday = datetime.date(1988, 6, 21)
        lifespan = 80
        command.run(name, birthday, lifespan)

        assert command.calendar_repo.save.call_count == 1
