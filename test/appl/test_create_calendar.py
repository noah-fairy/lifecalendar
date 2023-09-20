import datetime

from src.appl.container import Container
from src.appl.create_calendar import CreateCalendar
from src.infra.db.mapper import map_between_model_and_schema


class TestCreateCalendar:
    def test_run(self):
        map_between_model_and_schema()
        container = Container()
        container.compose()
        command = container.resolve(CreateCalendar)

        name = "고도"
        birthday = datetime.date(1988, 6, 21)
        lifespan = 80
        command.run(name, birthday, lifespan)
