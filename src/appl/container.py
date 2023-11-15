from src.appl.auth.sign_in_password import SignInPassword
from src.appl.auth.sign_in_token import SignInToken
from src.appl.auth.sign_out import SignOut
from src.appl.auth.sign_up import SignUp
from src.appl.cal.create_calendar import CreateCalendar
from src.appl.cal.create_period import CreatePeriod
from src.appl.cal.get_calendar import GetCalendar
from src.appl.cal.get_calendar_list import GetCalendarList
from src.appl.cal.update_calendar import UpdateCalendar
from src.appl.i_container import IContainer
from src.config import config
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_db_context import IDBContext
from src.domain.repo.i_user_repo import IUserRepo
from src.infra.repo.sa import SA
from src.infra.repo.sa_calendar_repo import SACalendarRepo
from src.infra.repo.sa_context import SAContext
from src.infra.repo.sa_user_repo import SAUserRepo


class Container(IContainer):
    def compose_by_env(self) -> None:
        # repository
        self.register(SA(config.DATABASE_URL, {}))
        self.register(SAContext(self.resolve(SA)))
        self.register(SACalendarRepo(self.resolve(SA)))
        self.register(SAUserRepo(self.resolve(SA)))

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
        self.register(
            CreatePeriod(self.resolve(IDBContext), self.resolve(ICalendarRepo))
        )

        self.register(SignUp(self.resolve(IDBContext), self.resolve(IUserRepo)))
        self.register(SignInPassword(self.resolve(IDBContext), self.resolve(IUserRepo)))
        self.register(SignInToken(self.resolve(IDBContext), self.resolve(IUserRepo)))
        self.register(SignOut(self.resolve(IDBContext), self.resolve(IUserRepo)))


container = Container()


def compose_container():
    global container
    container.compose()
