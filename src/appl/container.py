from src.appl.create_calendar import CreateCalendar
from src.appl.get_calendar import GetCalendar
from src.appl.get_calendar_list import GetCalendarList
from src.appl.i_container import IContainer
from src.appl.update_calendar import UpdateCalendar
from src.config import config
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext
from src.infra.repo.sa import SA
from src.infra.repo.sa_calendar_repo import SACalendarRepo
from src.infra.repo.sa_context import SAContext


class Container(IContainer):
    def compose_by_env(self) -> None:
        # repository
        self.register(SA(config.DATABASE_URL, {}))
        self.register(SAContext(self.resolve(SA)))
        self.register(SACalendarRepo(self.resolve(SA)))

    def compose(self) -> None:
        self.compose_by_env()

        # application
        self.register(
            GetCalendar(self.resolve(IDBContext), self.resolve(ICalendarRepo))
        )
        self.register(
            GetCalendarList(self.resolve(IDBContext), self.resolve(ICalendarRepo))
        )
        self.register(
            CreateCalendar(self.resolve(IDBContext), self.resolve(ICalendarRepo))
        )
        self.register(
            UpdateCalendar(self.resolve(IDBContext), self.resolve(ICalendarRepo))
        )


container = Container()


def compose_container():
    global container
    container.compose()
