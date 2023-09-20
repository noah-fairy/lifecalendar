from src.appl.create_calendar import CreateCalendar
from src.appl.i_container import IContainer
from src.infra.repo.sa import SA
from src.infra.repo.sa_calendar_repo import SACalendarRepo
from src.infra.repo.sa_context import SAContext


class Container(IContainer):
    def compose(self) -> None:
        # repository
        self.register(SA("postgresql://qodot@localhost/lifecalendar", {}))
        self.register(SAContext(self.resolve(SA)))
        self.register(SACalendarRepo(self.resolve(SA)))

        # application
        self.register(
            CreateCalendar(self.resolve(SAContext), self.resolve(SACalendarRepo))
        )
