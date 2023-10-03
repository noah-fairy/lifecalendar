from unittest.mock import MagicMock

from src.appl.container import Container
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext


class TestContainer(Container):
    def compose_by_env(self) -> None:
        # repository
        self.register(MagicMock(spec_set=IDBContext))
        self.register(MagicMock(spec_set=ICalendarRepo))


container = TestContainer()


def compose_container():
    global container
    container.compose()
