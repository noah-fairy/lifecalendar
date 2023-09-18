import datetime

from src.appl.create_calendar import CreateCalendar
from src.infra.db.mapper import map_between_model_and_schema
from src.infra.repo.sa import SA
from src.infra.repo.sa_calendar_repo import SACalendarRepo
from src.infra.repo.sa_context import SAContext


class TestCreateCalendar:
    def test_run(self):
        map_between_model_and_schema()

        sa = SA("postgresql://qodot@localhost/lifecalendar", {})
        db_context = SAContext(sa)
        calendar_repo = SACalendarRepo(sa)
        command = CreateCalendar(db_context, calendar_repo)

        name = "고도"
        birthday = datetime.date(1988, 6, 21)
        lifespan = 80
        command.run(name, birthday, lifespan)
